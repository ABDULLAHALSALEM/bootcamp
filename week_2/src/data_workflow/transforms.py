import pandas as pd

def enforce_schema(df: pd.DataFrame) -> pd.DataFrame:
    return df.assign(
        order_id=df["order_id"].astype("string"),
        user_id=df["user_id"].astype("string"),
        amount=pd.to_numeric(df["amount"], errors="coerce").astype("Float64"),
        quantity=pd.to_numeric(df["quantity"], errors="coerce").astype("Int64"),
    )

def missingness_report(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.isna().sum()
        .rename("n_missing")
        .to_frame()
        .assign(p_missing=lambda t: t["n_missing"] / len(df))
        .sort_values("p_missing", ascending=False)
    )

def normalize_text(s: pd.Series) -> pd.Series:
    import re
    _ws = re.compile(r"\s+")
    return (
        s.astype("string")
        .str.strip()
        .str.casefold()
        .str.replace(_ws, " ", regex=True)
    )
def apply_mapping(s: pd.Series, mapping: dict[str, str]) -> pd.Series:
    """1-Map values using a dictionary
    2-Values not in mapping stay unchanged"""

    return s.map(mapping).fillna(s)

def dedupe_keep_latest(df: pd.DataFrame, key_cols: list[str], ts_col: str) -> pd.DataFrame:
    """1-Sort by timestamp
    2-Remove duplicates, keeping the latest row
    3-Reset index"""
    df_sorted = df.sort_values(ts_col)
    deduped = df_sorted.drop_duplicates(subset=key_cols, keep="last")
    return deduped.reset_index(drop=True)