# Python for Data Manipulation (pandas), Visualisation (matplotlib), "Github"

import pandas as pd
import numpy as np

# Create a DataFrame
n=300
# Read from local file (read from laptop)
# df = pd.read_csv, read_excel
df = pd.DataFrame({
    "date": pd.date_range("2025-01-01", periods=n, freq="D"),
    "region": np.random.choice(["A", "B", "C", "D"], size=n),
    "products": np.random.choice(["Apple", "Orange", "Tea", "Coffee"], size=n),
    "unit": np.random.randint(1, 40, size=n),
    "price": np.random.choice([3, 3.50, 4.50, 6.80])
})

print(df)

# Create new column
df['revenue'] = df['unit']*df['price'] # Create a new variable/column, new_var = unit x price
df.head() # (): display first 5, df.head(10): display first 10

df.shape # return (rows, columns) - check dimension
df.info() # return general information about the dataset, such as col-name, data types (int, float, char), missing value

# Filter row = "where"
region = df[df['region'] == "A"]

# Criteria Unit > 30, price > 4
Cust = df[(df['unit'] > 30) & (df['price'] > 4)] # & = AND, / = or

# Group & Aggregate - group_by
by_region = df.groupby('region')['revenue'].sum().sort_values(ascending=False)
df.groupby('products')['revenue'].agg(['sum', 'mean', 'count'])

# Pivot Table
pivot_1 = df.pivot_table(index='region', columns='products', values='revenue', aggfunc='sum')
print(pivot_1)

# Visualisation
import matplotlib.pyplot as plt # matLab Library
import seaborn as sns # Seaborn Library

sns.set_theme(style="whitegrid")

# Bar graph
by_region.plot(kind='bar', color ='blue')
plt.title("Revenue by Region")
plt.ylabel("Revenue")
plt.xlabel("Region")
plt.show()

# Line graph
by_region.plot(kind='line', marker ='x')
plt.title("Revenue by Region")
plt.ylabel("Revenue")
plt.xlabel("Region")
plt.show()

# Scatter plot
sns.scatterplot(data=df, x='unit', y='revenue')
plt.title("Revenue vs. Unit by Region")
plt.ylabel("Revenue")
plt.xlabel("Unit")
plt.show()