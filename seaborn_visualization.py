import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("house_prices.csv")
print(data)


# Heatmap (Correlation Story)
plt.figure(figsize=(8, 5))

sns.heatmap(
    data.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap of House Price Factors")
plt.show()


# Pairplot (Multiple Relationships)
sns.pairplot(data)

plt.suptitle("Pairplot of House Price Dataset", y=1.02)
plt.show()

# Seaborn Style (Professional Look)
sns.set_style("whitegrid")
