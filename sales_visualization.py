# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load dataset
data = pd.read_csv("sales_data.csv")

sns.set(style="whitegrid")


# CHART 1: Trend - Monthly Sales
plt.figure()
sns.lineplot(x="Month", y="Sales", hue="Category", data=data, marker="o")
plt.title("Monthly Sales Trend by Category")
plt.ylabel("Sales (INR)")
plt.show()


# CHART 2: Comparison - Category Sales
plt.figure()
sns.barplot(x="Category", y="Sales", data=data)
plt.title("Average Sales by Category")
plt.show()


# CHART 3: Relationship - Sales Distribution
plt.figure()
sns.scatterplot(x="Month", y="Sales", hue="Category", data=data, s=100)
plt.title("Sales Distribution Across Months")
plt.show()


# CHART 4: Outliers - Box Plot
plt.figure()
sns.boxplot(x="Category", y="Sales", data=data)
plt.title("Sales Outliers by Category")
plt.show()
