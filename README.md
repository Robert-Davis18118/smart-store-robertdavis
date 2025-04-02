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
