import pandas as pd
import sqlite3
import pathlib
import sys

# For local imports, temporarily add project root to sys.path
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Constants
DW_DIR = pathlib.Path("data").joinpath("dw")
DB_PATH = DW_DIR.joinpath("smart_sales.db")
PREPARED_DATA_DIR = pathlib.Path("data").joinpath("prepared")

def create_schema(cursor: sqlite3.Cursor) -> None:
    """Create tables in the data warehouse if they don't exist."""
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer (
            customer_id INTEGER PRIMARY KEY,
            name TEXT,
            region TEXT,
            join_date TEXT,
            loyalty_points INTEGER,
            gender TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT,
            category TEXT,
            unit_price REAL,
            stock_quantity INTEGER,
            supplier TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sale (
            transaction_id INTEGER PRIMARY KEY,
            sale_date TEXT,
            customer_id INTEGER,
            product_id INTEGER,
            store_id INTEGER,
            campaign_id INTEGER,
            sale_amount REAL,
            discount_percent REAL,
            payment_type TEXT,
            FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
            FOREIGN KEY (product_id) REFERENCES product (product_id)
        )
    """)

def insert_customers(customers_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    customers_df = customers_df.rename(columns={
        "CustomerID": "customer_id",
        "Name": "name",
        "Region": "region",
        "JoinDate": "join_date",
        "LoyaltyPoints": "loyalty_points",
        "Gender": "gender"
    })
    customers_df.to_sql("customer", cursor.connection, if_exists="append", index=False)

def insert_products(products_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    products_df = products_df.rename(columns={
        "ProductID": "product_id",
        "ProductName": "product_name",
        "Category": "category",
        "UnitPrice": "unit_price",
        "StockQuantity": "stock_quantity",
        "Supplier": "supplier"
    })
    products_df.to_sql("product", cursor.connection, if_exists="append", index=False)

def insert_sales(sales_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    sales_df = sales_df.rename(columns={
        "TransactionID": "transaction_id",
        "SaleDate": "sale_date",
        "CustomerID": "customer_id",
        "ProductID": "product_id",
        "StoreID": "store_id",
        "CampaignID": "campaign_id",
        "SaleAmount": "sale_amount",
        "DiscountPercent": "discount_percent",
        "PaymentType": "payment_type"
    })
    sales_df.to_sql("sale", cursor.connection, if_exists="append", index=False)

def load_data_to_db() -> None:
    DW_DIR.mkdir(parents=True, exist_ok=True)
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        create_schema(cursor)

        customers_df = pd.read_csv(PREPARED_DATA_DIR / "customers_data_prepared.csv")
        products_df = pd.read_csv(PREPARED_DATA_DIR / "products_data_prepared.csv")
        sales_df = pd.read_csv(PREPARED_DATA_DIR / "sales_data_prepared.csv")

        insert_customers(customers_df, cursor)
        insert_products(products_df, cursor)
        insert_sales(sales_df, cursor)

        conn.commit()
        print("✅ Data warehouse created and loaded successfully.")
    except Exception as e:
        print(f"❌ Error loading data: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    load_data_to_db()
