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

## Images 1
![This is an alt text.](reports\figures\revenue_by_country.png)


## Images 2
![This is an alt text.](reports\figures\revenue_trend_monthly.png)

## Images 3
![This is an alt text.](reports\figures\amount_hist_winsor.png)



## Images 4
![This is an alt text.](reports\figures\date_per_amount.png)



## Images run_day1_load
![This is an alt text.](reports\figures\run_day1_load.png)

## Images run_day2_clean
![This is an alt text.](reports\figures\run_day2_clean.png)

## Images run_day3_build_analytics
![This is an alt text.](reports\figures\run_day3_build_analytics.png)

## Images run_etl
![This is an alt text.](reports\figures\run_etl.png)
