import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import os

# Connect to SQLite data warehouse
conn = sqlite3.connect("data/dw/smart_sales.db")

# Query data from joined tables without extracting the month in SQL
query = """
    SELECT 
        p.category, 
        c.region, 
        s.sale_date,
        s.sale_amount
    FROM sale s
    JOIN customer c ON s.customer_id = c.customer_id
    JOIN product p ON s.product_id = p.product_id
"""

# Read the query result into a DataFrame
df = pd.read_sql_query(query, conn)

# Convert sale_date to datetime and extract month
df["sale_date"] = pd.to_datetime(df["sale_date"], errors='coerce')
df["month"] = df["sale_date"].dt.month

# Preview to make sure conversion worked
print("\n🔍 Preview of joined and processed data:")
print(df.head())

# Group and aggregate the data
result = df.groupby(["category", "region", "month"]).agg(total_sales=("sale_amount", "sum")).reset_index()

# Show aggregated data
print("\n✅ Aggregated result:")
print(result.head())

# Save the result to a CSV file
os.makedirs("data/olap", exist_ok=True)
result.to_csv("data/olap/custom_bi_output.csv", index=False)

# Create and save the bar chart
plt.figure(figsize=(10, 6))
sns.barplot(data=result, x="category", y="total_sales", hue="region")
plt.title("Sales by Product Category and Region")
plt.xticks(rotation=45)
plt.tight_layout()

# Save image
os.makedirs("images", exist_ok=True)
plt.savefig("images/p7_sales_by_category_region.png")
plt.show()
