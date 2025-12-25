# Data Workflow

This project implements a simple and structured data workflow for loading,
validating, and processing CSV data into a clean Parquet format.

The project is designed to demonstrate:
- Clear project structure
- Reusable Python modules
- Safe data loading and transformation
- Simple batch execution using a runner script

--------------------------------------------------

## Project Structure

```text
data-workflow/
├─ README.md
├─ pyproject.toml
├─ run_day1_load.py
├─ data/
│  ├─ raw/
│  │  └─ users.csv
│  ├─ cache/
│  ├─ processed/
│  │  └─ users.parquet
│  └─ external/
└─ src/
   └─ data_workflow/
      ├─ __init__.py
      ├─ config.py
      ├─ io.py
      └─ transforms.py
```

<<<<<<< HEAD
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
=======

## All Required Python Source Files

- **run_day1_load.py**  
  Entry-point script that executes the Day 1 data loading workflow.

- **src/data_workflow/config.py**  
  Centralized and immutable project path configuration.

- **src/data_workflow/io.py**  
  Handles CSV reading and Parquet writing operations.

- **src/data_workflow/transforms.py**  
  Applies schema enforcement and data type normalization.

- **src/data_workflow/__init__.py**  
  Marks the data_workflow directory as a Python package.

---

## Requirements

- Python 3.11
- pandas
- pyarrow
- uv

---

## After Cloning the Repository, Install Them Using

```bash
uv sync
```

## How to Run (`run_day1_load.py`)

The `run_day1_load.py` script performs the Day 1 data loading process.  
It reads raw CSV data, enforces the schema, and writes the processed  
output in Parquet format.

---

### Prerequisites

Make sure all dependencies are installed:

```bash
uv sync
```
### Run Location

All commands must be executed from the project root directory:

```text
data-workflow/
├─ run_day1_load.py
├─ src/
└─ data/
```

### Running the Script

Execute the workflow using `uv`:

```bash
uv run python run_day1_load.py
```

### Notes

- Ensure the input file exists at:
  ```text
  data/raw/users.csv
```

- Output directories are created automatically if missing.
- Invalid numeric values are safely coerced to `NaN`.
- The workflow is designed to be simple, reproducible, and safe.

>>>>>>> f44c850812bb27b30da30e2e72f03ce2f4bd011a
