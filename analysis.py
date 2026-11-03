from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "retail_sales.csv"
OUTPUT_DIR = ROOT / "outputs"
REQUIRED = {"order_id", "order_date", "region", "category", "product", "quantity", "unit_price_inr", "discount_pct", "payment_method", "sales_amount_inr", "profit_amount_inr"}


def load_data(path=DATA_FILE):
    df = pd.read_csv(path, parse_dates=["order_date"])
    missing = REQUIRED.difference(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    if df["order_id"].duplicated().any():
        raise ValueError("Duplicate order IDs found")
    if df.isna().any().any():
        raise ValueError("Missing values found")
    if (df[["quantity", "unit_price_inr", "sales_amount_inr"]] < 0).any().any():
        raise ValueError("Negative quantity, price or sales found")
    if not df["discount_pct"].between(0, 1).all():
        raise ValueError("Discount must be between 0 and 1")
    return df


def build_summaries(df):
    data = df.copy()
    data["month"] = data["order_date"].dt.to_period("M").astype(str)
    orders = data["order_id"].nunique()
    kpis = pd.DataFrame([{
        "orders": orders,
        "units_sold": int(data["quantity"].sum()),
        "total_sales_inr": round(data["sales_amount_inr"].sum(), 2),
        "estimated_profit_inr": round(data["profit_amount_inr"].sum(), 2),
        "average_order_value_inr": round(data["sales_amount_inr"].sum() / orders, 2),
    }])
    return {
        "kpis": kpis,
        "sales_by_region": data.groupby("region", as_index=False)["sales_amount_inr"].sum().sort_values("sales_amount_inr", ascending=False),
        "sales_by_category": data.groupby("category", as_index=False)["sales_amount_inr"].sum().sort_values("sales_amount_inr", ascending=False),
        "monthly_sales": data.groupby("month", as_index=False)["sales_amount_inr"].sum().sort_values("month"),
        "payment_methods": data.groupby("payment_method", as_index=False)["order_id"].nunique().rename(columns={"order_id": "orders"}).sort_values("orders", ascending=False),
    }


def main():
    df = load_data()
    summaries = build_summaries(df)
    OUTPUT_DIR.mkdir(exist_ok=True)
    print(f"Loaded {len(df)} rows")
    for name, result in summaries.items():
        print(f"\n{name.upper()}\n{result.to_string(index=False)}")
        result.to_csv(OUTPUT_DIR / f"{name}.csv", index=False)
    print(f"\nSaved {len(summaries)} summary files to {OUTPUT_DIR}")
    print("Reminder: data is synthetic; profit is illustrative.")


if __name__ == "__main__":
    main()
