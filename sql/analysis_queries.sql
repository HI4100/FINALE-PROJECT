-- Import data/retail_sales.csv into a table named retail_sales first.
-- Synthetic practice dataset; profit values are illustrative estimates.

-- Overall KPIs
SELECT COUNT(DISTINCT order_id) AS orders, SUM(quantity) AS units_sold,
       ROUND(SUM(sales_amount_inr), 2) AS sales_inr,
       ROUND(SUM(profit_amount_inr), 2) AS estimated_profit_inr,
       ROUND(AVG(sales_amount_inr), 2) AS average_order_value_inr
FROM retail_sales;

-- Sales by region
SELECT region, ROUND(SUM(sales_amount_inr), 2) AS sales_inr
FROM retail_sales GROUP BY region ORDER BY sales_inr DESC;

-- Sales and estimated profit by category
SELECT category, ROUND(SUM(sales_amount_inr), 2) AS sales_inr,
       ROUND(SUM(profit_amount_inr), 2) AS estimated_profit_inr
FROM retail_sales GROUP BY category ORDER BY sales_inr DESC;

-- Monthly sales (SQLite)
SELECT strftime('%Y-%m', order_date) AS month,
       ROUND(SUM(sales_amount_inr), 2) AS sales_inr
FROM retail_sales GROUP BY month ORDER BY month;

-- Payment methods
SELECT payment_method, COUNT(DISTINCT order_id) AS orders
FROM retail_sales GROUP BY payment_method ORDER BY orders DESC;

-- Top products
SELECT product, SUM(quantity) AS units_sold,
       ROUND(SUM(sales_amount_inr), 2) AS sales_inr
FROM retail_sales GROUP BY product ORDER BY sales_inr DESC LIMIT 10;
