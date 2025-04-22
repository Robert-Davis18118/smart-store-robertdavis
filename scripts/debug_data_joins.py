import pandas as pd
import sqlite3

# Connect to your data warehouse
conn = sqlite3.connect(r"C:\Projects\smart-store-robertdavis\data\dw\smart_sales.db")

# Check if the 'sale' table has data
df_sale = pd.read_sql_query("SELECT * FROM sale", conn)
print(f"✅ Rows in sale table: {len(df_sale)}")

# Check if the 'product' table has data
df_product = pd.read_sql_query("SELECT * FROM product", conn)
print(f"✅ Rows in product table: {len(df_product)}")

# Check if the 'customer' table has data
df_customer = pd.read_sql_query("SELECT * FROM customer", conn)
print(f"✅ Rows in customer table: {len(df_customer)}")

# Test JOIN with product
df_product_join = pd.read_sql_query("""
    SELECT * FROM sale s
    JOIN product p ON s.product_id = p.product_id
""", conn)
print(f"🔗 Rows after JOIN with product: {len(df_product_join)}")

# Test JOIN with customer
df_customer_join = pd.read_sql_query("""
    SELECT * FROM sale s
    JOIN customer c ON s.customer_id = c.customer_id
""", conn)
print(f"🔗 Rows after JOIN with customer: {len(df_customer_join)}")

# Test full JOIN with product and customer
df_full_join = pd.read_sql_query("""
    SELECT * FROM sale s
    JOIN customer c ON s.customer_id = c.customer_id
    JOIN product p ON s.product_id = p.product_id
""", conn)
print(f"🔗 Rows after JOIN with product AND customer: {len(df_full_join)}")

# Optional: display the first few rows if available
if len(df_full_join) > 0:
    print("\nPreview of joined data:")
    print(df_full_join.head())
else:
    print("\n❌ No data returned from full join — check for orphaned product_id or customer_id.")
