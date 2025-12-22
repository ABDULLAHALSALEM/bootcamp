import logging
from pathlib import Path
import sys

from week_2.src.data_workflow.config import make_paths
from src.data_workflow.transforms import enforce_schema
from src.data_workflow.io import read_orders_csv, write_parquet

ROOT= Path(__file__).resolve().parent[1]
sys.path.append(str(ROOT / "src"))

loggers=logging.gitLogger(__name__)

Paths= make_paths(ROOT)

def main():
    df =read_orders_csv(Paths.raw / "users.csv")
    df = enforce_schema(df,'users')
    df= write_parquet(df, Paths.processed / "users.parquet")

    loggers.info("Row Count:", len (df))
    loggers.info("Paths:", Paths)  


if __name__ == "__main__":
    main()