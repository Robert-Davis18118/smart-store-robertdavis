import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to your SQLite database
DB_PATH = "data/dw/smart_sales.db"

# Connect to the database
conn = sqlite3.connect(DB_PATH)

# Query: Get total sales by product category, region, and month
query = """
SELECT 
    p.category AS product_category,
    c.region AS region,
    strftime('%m', s.sale_date) AS month,
    SUM(s.sale_amount) AS total_sales
FROM sale s
JOIN product p ON s.product_id = p.product_id
JOIN customer c ON s.customer_id = c.customer_id
GROUP BY p.category, c.region, month
ORDER BY total_sales DESC;
"""

# Load into DataFrame
df = pd.read_sql_query(query, conn)

# Show the first few rows
print(df.head())

# Save the result to CSV (optional)
df.to_csv("data/olap/top_category_by_region_month.csv", index=False)

# Close the connection
conn.close()
