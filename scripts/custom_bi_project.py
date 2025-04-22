import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import os

# Create output folder if it doesn't exist
os.makedirs("data/olap", exist_ok=True)
os.makedirs("images", exist_ok=True)

# Connect to SQLite
conn = sqlite3.connect("data/dw/smart_sales.db")

# Load data using JOIN
df = pd.read_sql_query("""
    SELECT 
        p.category, 
        c.region, 
        strftime('%m', s.sale_date) AS month,
        s.sale_amount
    FROM sale s
    JOIN customer c ON s.customer_id = c.customer_id
    JOIN product p ON s.product_id = p.product_id
""", conn)

# Group data
result = df.groupby(["category", "region", "month"]).agg(
    total_sales=pd.NamedAgg(column="sale_amount", aggfunc="sum")
).reset_index()

# Save the grouped data
result.to_csv("data/olap/custom_bi_output.csv", index=False)

# Plot bar chart
plt.figure(figsize=(10, 6))
sns.barplot(data=result, x="category", y="total_sales", hue="region")
plt.title("Sales by Product Category and Region")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/p7_sales_by_category_region.png")
plt.show()
