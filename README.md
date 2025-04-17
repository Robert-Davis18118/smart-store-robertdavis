# smart-store-robertdavis


.venv\Scripts\activate-------use to activate .venv

To set the VS Code Interpreter:

    Open the Command Palette: Press Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (Mac).
    Search for "Python: Select Interpreter":
    Type Python: Select Interpreter in the Command Palette search bar and select it from the dropdown.
    Choose an Interpreter - A list of available Python environments will appear. Look for the local .venv option.
    Once selected, check the Python version displayed in the bottom-left corner of the VS Code window in the status bar.
#3-17-25 added data_prep.py & logger.py. ran first python script "data_prep.py" reading previously supplied .csv files. 

### Data Preparation Scripts (P3)

- `data_prep_customers.py`: Cleans customer data (drops duplicates, removes missing, filters outliers)
- `data_prep_products.py`: Cleans product data
- `data_prep_sales.py`: Cleans sales data
## Data Warehouse (P4)

✅ Successfully created and loaded a star schema with one fact table (`sale`) and two dimension tables (`customer`, `product`).

### Schema Summary

- **customer**: Contains demographic and loyalty data
- **product**: Contains item details including price and supplier
- **sale**: Records transactions, including discounts and payment type

### Screenshot of Populated Tables

![Customer Table Screenshot](images/customer_table.png)
![Product Table Screenshot](images/product_table.png)
![Sale Table Screenshot](images/sale_table.png)
1# 📦 Project 6: OLAP BI Insights & Storytelling

## ✅ 1. The Business Goal

**Goal:** Identify the top-selling product category by region and month.  
**Why it matters:** This insight helps optimize inventory distribution, marketing focus, and sales strategies in different regions based on real customer buying behavior.

---

## 💾 2. Data Source

**Source:** `smart_sales.db` from `data/dw/`

**Tables Used:**
- `sales` – includes transaction data: `sale_date`, `sale_amount`, `product_id`, `region`
- `products` – includes: `product_id`, `product_category`

**Key Columns:**
- `sales.product_id`, `sales.sale_date`, `sales.sale_amount`, `sales.region`
- `products.product_category`

---

## 🧰 3. Tools

- **Language:** Python
- **Libraries:** `pandas`, `sqlite3`, `matplotlib`, `seaborn`
- **Why:** Python enabled full control over data analysis (OLAP logic), and matplotlib/seaborn generated clear, professional visualizations.

---

## ⚙️ 4. Workflow & Logic

**Step-by-Step Logic:**
1. Load data from SQLite using `pandas.read_sql()`
2. Merge `sales` and `products` on `product_id`
3. Extract month from `sale_date` column
4. Group by `product_category`, `region`, and `month`
5. Aggregate total `sale_amount`
6. Save results to `data/olap/top_category_by_region_month.csv`

**OLAP Techniques Applied:**
- **Slicing:** Focused on specific product categories
- **Dicing:** Broke down data by `region` and `month`
- **Drilldown:** Drilled from total sales → sales by month

---

## 📊 5. Results & Visualizations

**CSV Output:**  
`data/olap/top_category_by_region_month.csv`

**Python Chart Code:**
```python
sns.barplot(data=df, x="product_category", y="total_sales", hue="region")
plt.title("Top-Selling Product Category by Region")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
