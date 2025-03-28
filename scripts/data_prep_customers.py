import pandas as pd
from data_scrubber import DataScrubber

# Step 1: Load raw data
df = pd.read_csv("data/raw/customers_data.csv")

# Step 2: Clean the data
scrubber = DataScrubber(df)
scrubber.remove_duplicate_records()
scrubber.handle_missing_data(drop=True)
scrubber.filter_column_outliers(column="LoyaltyPoints", lower_bound=0, upper_bound=10000)
scrubber.convert_column_to_new_data_type("LoyaltyPoints", int)

# Step 3: Save the cleaned data
scrubber.df.to_csv("data/prepared/customers_data_prepared.csv", index=False)

print("✅ Customers data cleaned and saved.")
