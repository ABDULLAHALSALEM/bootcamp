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

def parse_datetime(df: pd.DataFrame, col: str, *, utc: bool = True) -> pd.DataFrame:
    """1-Convert text column to datetime using pd.to_datetime(..., errors="coerce", utc=utc)
        2-Use .assign() to update the column"""
    return df.assign(
        **{col: pd.to_datetime(df[col], errors="coerce", utc=True)}
    )


def add_time_parts(df: pd.DataFrame, ts_col: str) -> pd.DataFrame:
    """
    1-Extract: date, year, month, dow (day of week), hour
    2-Use .dt accessor (only works on datetime columns!)"""
    return df.assign(
        date=df[ts_col].dt.date,
        year=df[ts_col].dt.year,
        month=df[ts_col].dt.month,
        dow=df[ts_col].dt.dayofweek,
        hour=df[ts_col].dt.hour
    )

def add_missing_flags(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    out = df.copy()
    for c in cols:
        out[f"{c}__isna"] = out[c].isna()
    return out

def add_outlier_flag(df: pd.DataFrame, col: str, *, k: float = 1.5) -> pd.DataFrame:
    lo, hi = iqr_bounds(df[col], k=k)
    return df.assign(**{f"{col}__is_outlier": (df[col] < lo) | (df[col] > hi)})

def iqr_bounds(s: pd.Series, k: float = 1.5) -> tuple[float, float]:
    """1-Calculate IQR bounds: Q1 - k*IQR, Q3 + k*IQR
    2-Ignore missing values
    3-Return (lo, hi)"""
    non_missing = s.dropna()
    q1 = non_missing.quantile(0.25)
    q3 = non_missing.quantile(0.75)
    iqr = q3 - q1
    lo = q1 - k * iqr
    hi = q3 + k * iqr
    return lo, hi

def winsorize(s: pd.Series, lo: float = 0.01, hi: float = 0.99) -> pd.Series:
    """1-Cap values at given quantiles
    2-Ignore missing values
    3-Return modified Series"""
    non_missing = s.dropna()
    lower_bound = non_missing.quantile(lo)
    upper_bound = non_missing.quantile(hi)
    return s.clip(lower=lower_bound, upper=upper_bound)

