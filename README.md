# Atelier Retail Sales Analytics

A reproducible beginner-to-intermediate data analytics project using **Python, pandas, CSV and SQL**. The project explores retail order data, calculates sales and profit metrics, compares regions and product categories, and produces summary outputs.

## Dataset transparency

The included 360-row dataset is **synthetic practice data**, generated deterministically for this portfolio project. It is not real company or customer data. Profit values are illustrative estimates based on assumed category cost ratios. Findings must not be presented as real business performance.

## Questions explored

1. What are total sales, estimated profit and units sold?
2. Which regions and categories contribute the most sales?
3. How do sales vary by month?
4. What is the average order value?
5. Which payment methods are used most often?

## Project structure

```text
Atelier-Retail-Sales-Analytics/
├── data/retail_sales.csv
├── reports/initial_analysis.md
├── sql/analysis_queries.sql
├── analysis.py
├── requirements.txt
└── README.md
```

## Run locally

1. Install Python 3.10 or newer.
2. (Recommended) Create and activate a virtual environment.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run: `python analysis.py`.

The script reads the CSV, validates required columns and key fields, prints KPI summaries and writes CSV summaries into `outputs/`.

## Tools and skills

- Python and pandas for data loading, validation and aggregation
- Data cleaning and derived metrics
- Grouping, sorting and monthly trend analysis
- SQL aggregation queries
- Reproducible reporting and GitHub documentation

## Limitations

- Data is synthetic and designed for learning.
- No causal conclusions or forecasting are claimed.
- Profit is an illustrative estimate, not audited accounting profit.
- No dashboard is included in this first version.

## Author

Humza Warsi | [GitHub: HI4100](https://github.com/HI4100)
