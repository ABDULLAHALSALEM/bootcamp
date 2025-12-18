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
```text
csv-profiler/
├─ README.md
├─ pyproject.toml
├─ data/
│  └─ sample.csv
├─ outputs/
│  ├─ report.json
│  └─ report.md
└─ src/
   └─ csv_profiler/
      ├─ __init__.py
      ├─ io.py
      ├─ profile.py
      ├─ render.py
      ├─ cli.py
      └─ app.py
```
-------------

**What to Include / Exclude in the Repository**

Include

- README.md

- src/

- data/

- outputs/

- pyproject.toml

- All required Python source files

**Exclude**

- .venv/

- __pycache__/

- OS files (e.g. .DS_Store)

***(Handled using .gitignore)***

----------------------

**Requirements**

- Python 3.11

- uv

- Typer

- Streamlit

**Install dependencies if needed:**
- uv pip install typer streamlit

**How to Run the Project**
1) Using CLI (Typer)

From the project root directory:
- uv run python -m csv_profiler.cli data/sample.csv --out outputs/



**This will:**

- Read the CSV file

- Generate profiling statistics

- Save:

  - outputs/report.json

  - outputs/report.md


**To view CLI help:**
- uv run python -m csv_profiler.cli --help

-------------

**2) Using Streamlit GUI**

From the project root directory:
- streamlit run src/csv_profiler/app.py

***Important:***

-  run Streamlit from inside src/

------------------

**Streamlit Usage**

1- Upload a CSV file

2-(Optional) Preview the data

3-Click Generate report

4-Download JSON or Markdown

5-Save outputs locally

