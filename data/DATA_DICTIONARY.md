# Data Dictionary

The source file is `data/retail_sales.csv`. It contains 360 synthetic order-level records.

| Column | Type | Description |
|---|---|---|
| order_id | Text | Unique synthetic order identifier. |
| order_date | Date | Order date in YYYY-MM-DD format, within 2025. |
| region | Category | Synthetic sales region: North, South, East or West. |
| category | Category | Product category. |
| product | Text | Product name. |
| quantity | Integer | Number of units in the order line. |
| unit_price_inr | Decimal | Listed unit price in Indian rupees. |
| discount_pct | Decimal | Discount fraction, from 0.00 to 0.20. |
| payment_method | Category | UPI, Card, Cash or Net Banking. |
| sales_amount_inr | Decimal | Quantity × unit price × (1 − discount). |
| profit_amount_inr | Decimal | Illustrative estimated profit using an assumed product-category cost ratio. |

## Important assumptions

- Each row represents one order line; in this generated dataset, each order ID appears once.
- Sales amount is calculated after discount.
- Profit is not real accounting profit. It is calculated from assumed category-level cost percentages and is included only to practise analysis.
- All customer, transaction and business information is synthetic; no personal data is included.
