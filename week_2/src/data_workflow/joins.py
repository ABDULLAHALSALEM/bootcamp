from __future__ import annotations
from turtle import left
import pandas as pd


def safe_left_join(left: pd.DataFrame,right: pd.DataFrame,on: str | list[str],*,validate: str,suffixes: tuple[str, str] = ("", "_r"),) -> pd.DataFrame:
    # Left-join with enforced join cardinality via `validate=`. -Wrapper around pd.merge() with validate parameter -Prevents join explosions by checking cardinality -validate="many_to_one": left can have duplicates, right must be unique
    validate_options = {"many_to_one", "one_to_one"}
    if validate not in validate_options:
        raise ValueError(f"Invalid validate option: {validate}. Must be one of {validate_options}")
    return left.merge(
        right,
        how="left",
        on=on,
        validate=validate,
        suffixes=suffixes,
    )



