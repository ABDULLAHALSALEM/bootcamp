# Summary of Findings and Caveats

## Key Findings

- **Finding 1 (quantified)**: Saudi Arabia (SA) accounts for nearly all recorded revenue, totaling approximately 145, while AE contributes negligible or zero revenue in the current dataset.
- **Finding 2 (quantified)**: Order amounts are highly skewed; most values fall between 8 and 25, with a single high-value order near 100 that materially impacts aggregate metrics.
- **Finding 3 (quantified)**: Average order value is driven upward by one outlier; after winsorization, the highest observed amount is reduced to approximately 97.75 for visualization stability.
- **Finding 4 (quantified)**: Revenue activity is limited to early December 2025, with too few observations to establish a statistically meaningful monthly trend.

## Definitions

- **Revenue**: Sum of `amount` for orders where `status_clean == "paid"`.
- **AOV (Average Order Value)**: Mean of non-null values in the `amount` column.
- **Refund rate**: Proportion of orders where `status_clean == "refund"`.
- **Time window**: Early December 2025, based on available `created_at` values.
- **Winsorized amount**: Order amounts capped at upper bounds to reduce the influence of extreme outliers in visualizations.

## Data Quality Caveats

### Missingness
- Some orders have missing `amount` values, resulting in their exclusion from revenue and AOV calculations.
- At least one order has a missing or invalid `created_at` value (`NaT`), preventing inclusion in time-based analyses.

### Duplicates
- No explicit duplicate orders were identified in the provided dataset.

### Join Coverage
- Country-level results depend on successful joins with the users table; unmatched records may bias country comparisons, particularly given the small sample size.

### Outliers
- One order with an amount near 100 was identified as an outlier; charts use winsorized values for readability, while raw values are retained for totals.

### Other Issues
- Order status values appear in multiple formats (`Paid`, `paid`, `PAID`, `Refund`) and required normalization into `status_clean`.

## Next Questions

- How does the refund rate evolve as additional data becomes available?
- Does average order value vary by customer country or signup date?
- Are higher-value orders associated with specific days or hours?
- How do revenue patterns change once data volume increases beyond December 2025?

## Technical Notes

- **ETL Pipeline**: Run `uv run python scripts/run_etl.py` to reproduce processed outputs.
- **Run Metadata**: See `data/processed/_run_meta.json` for execution details.
- **Data Source**: Raw data is stored in `data/raw/`, with processed outputs in `data/processed/`.
- **EDA Notebook**: See `notebooks/eda.ipynb` for detailed exploratory analysis.
