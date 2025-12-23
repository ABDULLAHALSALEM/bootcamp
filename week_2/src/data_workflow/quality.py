import pandas as pd

def require_columns(df: pd.DataFrame, cols: list[str]) -> None:
    missing_cols = [col for col in cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    
def assert_non_empty(df: pd.DataFrame, name: str = "df") -> None:
    if df.empty:
        raise ValueError(f"The DataFrame '{name}' is empty.")

def assert_unique_key(df: pd.DataFrame, key: str, *, allow_na: bool = False) -> None:
    """1-Check that a column contains unique values
    2-Check for missing values if allow_na=False
    3-Raise AssertionError if duplicates or missing values found"""
    
    if not allow_na:
        if df[key].isna().any():
            raise ValueError(f"Column '{key}' contains missing values.")
    
    duplicates = df[df.duplicated(subset=[key], keep=False)]
    if not duplicates.empty:
        raise ValueError(f"Column '{key}' contains duplicate values:\n{duplicates}")


def assert_in_range(s: pd.Series, lo=None, hi=None, name: str = "value") -> None:
    """1-Check that all values are within a range
    2-Ignore missing values (only check non-missing)
    3-Raise AssertionError if values are outside range"""

    non_missing = s.dropna()
    if lo is not None:
        below_lo = non_missing[non_missing < lo]
        if not below_lo.empty:
            raise ValueError(f"Values in '{name}' below {lo}:\n{below_lo}")
    if hi is not None:
        above_hi = non_missing[non_missing > hi]
        if not above_hi.empty:
            raise ValueError(f"Values in '{name}' above {hi}:\n{above_hi}")
