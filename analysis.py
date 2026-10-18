from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Find the CSV file in the same folder as this Python script.
PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "sales_data.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# 1. Load the sales data.
df = pd.read_csv(DATA_FILE)
print("\n--- First five rows ---")
print(df.head())

# 2. Check and clean the data.
print("\n--- Dataset information ---")
print(df.info())
print("\nMissing values before cleaning:")
print(df.isnull().sum())

df = df.drop_duplicates()
df = df.dropna(subset=["OrderID", "Date", "Product", "Quantity", "Price"])
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df = df.dropna(subset=["Date", "Quantity", "Price"])
df = df[(df["Quantity"] > 0) & (df["Price"] >= 0)]

# 3. Calculate revenue for each order row.
df["Revenue"] = df["Quantity"] * df["Price"]
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# 4. Print useful business metrics.
total_revenue = df["Revenue"].sum()
total_units = df["Quantity"].sum()
total_orders = df["OrderID"].nunique()
average_order_value = total_revenue / total_orders if total_orders else 0

print("\n--- Sales summary ---")
print(f"Total revenue: ₹{total_revenue:,.2f}")
print(f"Total units sold: {total_units:,.0f}")
print(f"Number of orders: {total_orders}")
print(f"Average revenue per order: ₹{average_order_value:,.2f}")

product_revenue = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
product_quantity = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
monthly_revenue = df.groupby("Month")["Revenue"].sum().sort_index()
category_revenue = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

print("\n--- Revenue by product ---")
print(product_revenue.to_string())
print("\n--- Units sold by product ---")
print(product_quantity.to_string())
print("\n--- Revenue by category ---")
print(category_revenue.to_string())
print("\n--- Monthly revenue ---")
print(monthly_revenue.to_string())

print(f"\nHighest-revenue product: {product_revenue.idxmax()}")
print(f"Most units sold: {product_quantity.idxmax()}")
print(f"Highest-revenue month: {monthly_revenue.idxmax()}")

# 5. Save analysis results.
product_revenue.rename("Revenue").to_csv(OUTPUT_DIR / "revenue_by_product.csv")
monthly_revenue.rename("Revenue").to_csv(OUTPUT_DIR / "monthly_revenue.csv")

# 6. Create charts and save them in the outputs folder.
plt.figure(figsize=(9, 5))
product_revenue.sort_values().plot(kind="barh")
plt.title("Total Revenue by Product")
plt.xlabel("Revenue (₹)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "revenue_by_product.png", dpi=150)
plt.close()

plt.figure(figsize=(9, 5))
monthly_revenue.plot(kind="line", marker="o")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_revenue.png", dpi=150)
plt.close()

print(f"\nCharts and result files saved to: {OUTPUT_DIR}")
print("Analysis completed successfully.")
