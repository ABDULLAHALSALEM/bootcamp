#!/usr/bin/env python3
import logging
from pathlib import Path
import sys

# --- Setup ROOT and sys.path first ---
ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT / "src"))

from data_workflow.config import make_paths
from data_workflow.transforms import enforce_schema
from data_workflow.io import read_orders_csv, write_parquet

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")

paths = make_paths(ROOT)


def main() -> None:
    df = read_orders_csv(paths.raw / "users.csv")
    df = enforce_schema(df)  

    write_parquet(df, paths.processed / "users.parquet")

    logger.info("Row Count: %s", len(df))
    logger.info("Paths: %s", paths)


if __name__ == "__main__":
    main()