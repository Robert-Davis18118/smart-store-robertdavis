import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("data/olap/top_category_by_region_month.csv")

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="region", y="total_sales", hue="product_category")

plt.title("Top Product Category Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()

# Show the chart
plt.show()
