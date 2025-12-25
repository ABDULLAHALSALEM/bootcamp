'''Create a script that:
1. Loads raw CSVs
2. Runs quality checks (columns, non-empty)
3. Enforces schema
4. Creates missingness report → saves to `reports/missingness_orders.csv`
5. Normalizes status field → creates `status_clean`
6. Adds missing flags for `amount` and `quantity`
7. Validates ranges (amount >= 0, quantity >= 0)
8. Writes `orders_clean.parquet`'''
#!/usr/bin/env python3
import logging
import sys
from pathlib import Path
import pandas as pd
# make `src/` importable when running as a script
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from data_workflow.config import make_paths
from data_workflow.io import read_orders_csv, read_users_csv, write_parquet
from data_workflow.transforms import (
    enforce_schema,
    missingness_report,
    normalize_text,
    apply_mapping,
    add_missing_flags,
)
from data_workflow.quality import (
    require_columns,
    assert_non_empty,
    assert_in_range,
)

log = logging.getLogger(__name__)

def main() -> None:
    
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    p = make_paths(Path(__file__).resolve().parents[1])
    
    log.info("Loading raw inputs")
    orders_raw = read_orders_csv(p.raw / "orders.csv")
    users = read_users_csv(p.raw / "users.csv")
    log.info("Rows: orders_raw=%s, users=%s", len(orders_raw), len(users))

    require_columns(orders_raw,
    ["order_id","user_id","amount","quantity","created_at","status"])
    require_columns(users, ["user_id","country","signup_date"])
    assert_non_empty(orders_raw, "orders_raw")
    assert_non_empty(users, "users")


    orders = enforce_schema(orders_raw)

    rep = missingness_report(orders)
    reports_dir = ROOT / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    rep_path = reports_dir / "missingness_orders.csv"
    rep.to_csv(rep_path, index=True)

    log.info("Wrote missingness report: %s", rep_path)

    status_norm = normalize_text(orders["status"])
    mapping = {"paid": "paid", "refund": "refund", "refunded": "refund"}
    status_clean = apply_mapping(status_norm, mapping)

    orders_clean = (
        orders.assign(status_clean=status_clean)
        .pipe(add_missing_flags, cols=["amount", "quantity"])
    )

    
    assert_in_range(orders_clean["amount"], 0, None, "amount")
    assert_in_range(orders_clean["quantity"], 0, None, "quantity")

    write_parquet(orders_clean, p.processed / "orders_clean.parquet")
    write_parquet(users, p.processed / "users.parquet")
    log.info("Wrote processed outputs: %s", p.processed)


if __name__ == "__main__":
    main()


