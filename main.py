import pandas as pd
import matplotlib.pyplot as plt
import os

# Create output folder if not exists
os.makedirs("outputs/charts", exist_ok=True)

# Load dataset
df = pd.read_csv("data/superstore.csv", encoding='latin1')

print("✅ Data Loaded Successfully")
print(df.head())

# -----------------------------
# DATA CLEANING
# -----------------------------
df = df.dropna()

# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'])

print("✅ Data Cleaned")

# -----------------------------
# 1. SALES OVER TIME
# -----------------------------
sales_trend = df.groupby('Order Date')['Sales'].sum()

plt.figure()
sales_trend.plot()
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.savefig("outputs/charts/sales_trend.png")
plt.close()

# -----------------------------
# 2. TOP PRODUCTS
# -----------------------------
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure()
top_products.plot(kind='bar')
plt.title("Top 10 Products")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.savefig("outputs/charts/top_products.png")
plt.close()

# -----------------------------
# 3. CATEGORY ANALYSIS
# -----------------------------
category_sales = df.groupby('Category')['Sales'].sum()

plt.figure()
category_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales by Category")
plt.ylabel("")
plt.savefig("outputs/charts/category.png")
plt.close()

# -----------------------------
# 4. REGION ANALYSIS
# -----------------------------
region_sales = df.groupby('Region')['Sales'].sum()

plt.figure()
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.savefig("outputs/charts/region.png")
plt.close()

# -----------------------------
# 5. PROFIT ANALYSIS
# -----------------------------
plt.figure()
plt.scatter(df['Sales'], df['Profit'])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.savefig("outputs/charts/profit.png")
plt.close()

# -----------------------------
# BASIC INSIGHTS PRINT
# -----------------------------
print("\n📊 BASIC INSIGHTS:")

print(f"Total Sales: {df['Sales'].sum()}")
print(f"Total Profit: {df['Profit'].sum()}")

print("\nTop Product:")
print(top_products.head(1))

print("\nBest Category:")
print(category_sales.idxmax())

print("\nBest Region:")
print(region_sales.idxmax())

print("\n✅ Analysis Completed! Check 'outputs/charts' folder.")