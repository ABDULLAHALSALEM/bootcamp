from __future__ import annotations

import json
from pathlib import Path


def write_json(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",encoding="utf-8",
    )

# def write_markdown(report: dict, path: str | Path) -> None:
#     path = Path(path)
#     path.parent.mkdir(parents=True, exist_ok=True)

#     rows_count = report.get("rows", 0)
#     columns_dict = report.get("columns", {})  # dict: {col: {"missing": x, "non_empty": y}}

#     lines: list[str] = []
#     lines.append("# CSV Profiling Report\n")
#     lines.append(f"- Rows: **{rows_count}**")
#     lines.append(f"- Columns: **{len(columns_dict)}**\n")

#     lines.append("| Column | Missing |")
#     lines.append("|---|---:|")

#     for col_name, stats in columns_dict.items():
#         missing = stats.get("missing", 0)
#         lines.append(f"| {col_name} | {missing} |")

#     lines.append("") 

#     path.write_text("\n".join(lines) + "\n", encoding="utf-8")
              

def write_markdown(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    summary = report["summary"]
    columns = report["columns"]

    rows_count = summary["rows"]
    cols_count = summary["columns"]

    lines: list[str] = []

    lines.append("# CSV Profiling Report")
    lines.append("")

    lines.append("## Summary")
    lines.append(f"- Rows: **{rows_count}**")
    lines.append(f"- Columns: **{cols_count}**")
    lines.append("")

    lines.append("## Columns (table)")
    lines.append("| Column | Type | Missing % | Unique |")
    lines.append("|---|---|---:|---:|")

    for col_name, col in columns.items():
        col_type = col["type"]
        stats = col["stats"]
        missing = stats["missing"]
        unique = stats["unique"]
        missing_pct = (missing / rows_count * 100) if rows_count else 0

        lines.append(
            f"| {col_name} | {col_type} | {missing_pct:.1f}% | {unique} |"
        )

    lines.append("")

    lines.append("## Column details")

    for col_name, col in columns.items():
        col_type = col["type"]
        stats = col["stats"]

        lines.append(f"### `{col_name}`")
        lines.append(f"- Type: **{col_type}**")
        lines.append(f"- Count: **{stats['count']}**")
        lines.append(f"- Missing: **{stats['missing']}**")
        lines.append(f"- Unique: **{stats['unique']}**")
        lines.append("")

        if col_type == "number":
            lines.append(f"- Min: **{stats['min']}**")
            lines.append(f"- Max: **{stats['max']}**")
            lines.append(f"- Mean: **{stats['mean']}**")
        else:
            for item in stats["top"]:
                lines.append(f"- `{item['value']}`: {item['count']}")

        lines.append("")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
