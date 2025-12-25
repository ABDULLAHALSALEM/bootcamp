from __future__ import annotations
import logging
import sys
from pathlib import Path
import pandas as pd

# make `src/` importable when running as a script (no install required)
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from data_workflow.transforms import iqr_bounds
from data_workflow.config import make_paths
from data_workflow.quality import (
    require_columns,
    assert_non_empty,
    assert_unique_key,
)
from data_workflow.transforms import (
    parse_datetime,
    add_time_parts,
    winsorize,
)
from data_workflow.joins import safe_left_join


def add_outlier_flag(df: pd.DataFrame, col: str, *, k: float = 1.5) -> pd.DataFrame:
    lo, hi = iqr_bounds(df[col], k=k)
    return df.assign(**{f"{col}__is_outlier": (df[col] < lo) | (df[col] > hi)})

try:
    from bootcamp_data.transforms import add_outlier_flag

except ImportError:
    add_outlier_flag = None
    
log = logging.getLogger(__name__)



def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    p = make_paths(ROOT)

    orders = pd.read_parquet(p.processed / "orders_clean.parquet")
    users = pd.read_parquet(p.processed / "users.parquet")

    require_columns(
    orders,
        ["order_id", "user_id", "amount", "quantity", "created_at", "status_clean"],
    )
    require_columns(users, ["user_id", "country", "signup_date"])

    assert_non_empty(orders, "orders_clean")
    assert_non_empty(users, "users")
    assert_unique_key(users, "user_id")

    # time
    orders_t = (
        orders
        .pipe(parse_datetime, col="created_at", utc=True)
        .pipe(add_time_parts, ts_col="created_at")
    )
    n_missing_ts = int(orders_t["created_at"].isna().sum())
    log.info("missing created_at after parse: %s / %s", n_missing_ts, len(orders_t))

    joined = safe_left_join(
        orders_t,
        users,
        on="user_id",
        validate="many_to_one",
        suffixes=("", "_user"),
    )

    if len(joined) != len(orders_t):
        raise AssertionError("Row count changed on left join (join explosion?)")


    match_rate = 1.0 - float(joined["country"].isna().mean())
    log.info("rows=%s | country match rate=%.3f", len(joined), match_rate)


    joined = joined.assign(amount_winsor=winsorize(joined["amount"]))

    


    out_path = p.processed / "analytics_table.parquet"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    joined.to_parquet(out_path, index=False)
    log.info("wrote: %s", out_path)

if __name__ == "__main__":
    main()