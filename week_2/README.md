***CSV Profiler***
-
**Overview**

CSV Profiler is a Python project .
The project aims to analyze CSV files and generate structured profiling reports.

The project evolves gradually from simple Python scripts to a clean Python package with:

- Reusable functions

- Command-Line Interface (CLI) using Typer

- Graphical User Interface (GUI) using Streamlit

------------------------------
**Features**

- Read and analyze CSV files

- Detect missing values (empty, NA, null, etc.)

- Infer column data types (number / text)

- Compute statistics:

   - Numeric: count, missing, unique, min, max, mean

   - Text: count, missing, unique, top values

- Export reports as:

  - JSON

  - Markdown

- CLI support using Typer

- Interactive GUI using Streamlit

- Safe error handling (no Python tracebacks)
------------------

**Project Structure**

```
your-project/
├── data/
│   ├── raw/          # Immutable input data
│   ├── cache/        # Cached API responses
│   ├── processed/    # Clean, analysis-ready outputs
│   └── external/      # Reference data
├── src/
│   └── data_workflow/  # Your package (or project_name/)
│       └── __init__.py
├── scripts/          # Run scripts
├── reports/
│   └── figures/      # Exported charts
├── pyproject.toml    # Dependencies
├── README.md         # Project documentation
└── .gitignore        # Git ignore file
```

