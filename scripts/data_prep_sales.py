import pandas as pd
from data_scrubber import DataScrubber

# Step 1: Load raw data
df = pd.read_csv("data/raw/sales_data.csv")

# Step 2: Clean the data
scrubber = DataScrubber(df)
scrubber.remove_duplicate_records()
scrubber.handle_missing_data(drop=True)

# 👇 Convert column to integer before filtering
scrubber.convert_column_to_new_data_type("DiscountPercent", int)
scrubber.filter_column_outliers(column="DiscountPercent", lower_bound=0, upper_bound=100)

# Step 3: Save the cleaned data
scrubber.df.to_csv("data/prepared/sales_data_prepared.csv", index=False)

print("✅ Sales data cleaned and saved.")
