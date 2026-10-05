"""
Real-World Retail Sales Project
Run:
    pip install -r requirements.txt
    python analysis.py

Outputs are written to charts/ and output/.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "retail_sales_data.csv"
CHARTS = ROOT / "charts"
OUTPUT = ROOT / "output"
CHARTS.mkdir(exist_ok=True)
OUTPUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)

total_sales = df["Sales_INR"].sum()
total_profit = df["Profit_INR"].sum()
orders = df["Order_ID"].nunique()
avg_order = df["Sales_INR"].mean()
profit_margin = total_profit / total_sales * 100

monthly = df.groupby("Month", as_index=False)["Sales_INR"].sum()
category = df.groupby("Category", as_index=False).agg(Sales_INR=("Sales_INR","sum"), Profit_INR=("Profit_INR","sum"))
region = df.groupby("Region", as_index=False)["Sales_INR"].sum()
payment = df.groupby("Payment_Method", as_index=False)["Sales_INR"].sum()
top_products = df.groupby("Product", as_index=False).agg(Sales_INR=("Sales_INR","sum"), Quantity=("Quantity","sum")).sort_values("Sales_INR", ascending=False)

def bar(x, y, title, xlabel, ylabel, filename, rotation=0):
    plt.figure(figsize=(9,5))
    plt.bar(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotation)
    plt.tight_layout()
    plt.savefig(CHARTS / filename, dpi=160)
    plt.close()

plt.figure(figsize=(10,5))
plt.plot(monthly["Month"], monthly["Sales_INR"], marker="o")
plt.title("Monthly Retail Sales")
plt.xlabel("Month")
plt.ylabel("Sales (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(CHARTS / "01_monthly_sales.png", dpi=160)
plt.close()

bar(category["Category"], category["Sales_INR"], "Sales by Category", "Category", "Sales (INR)", "02_category_sales.png", 20)
bar(region["Region"], region["Sales_INR"], "Sales by Region", "Region", "Sales (INR)", "03_region_sales.png")
bar(payment["Payment_Method"], payment["Sales_INR"], "Sales by Payment Method", "Payment Method", "Sales (INR)", "04_payment_sales.png", 20)
bar(top_products.head(10)["Product"], top_products.head(10)["Sales_INR"], "Top 10 Products by Sales", "Product", "Sales (INR)", "05_top_products.png", 30)
bar(category["Category"], category["Profit_INR"], "Profit by Category", "Category", "Profit (INR)", "06_category_profit.png", 20)

summary = pd.DataFrame({
    "Metric": ["Total Sales (INR)", "Total Profit (INR)", "Number of Orders", "Average Order Value (INR)", "Profit Margin (%)"],
    "Value": [total_sales, total_profit, orders, avg_order, profit_margin]
})
summary.to_csv(OUTPUT / "kpi_summary.csv", index=False)
category.to_csv(OUTPUT / "category_summary.csv", index=False)
region.to_csv(OUTPUT / "region_summary.csv", index=False)
top_products.to_csv(OUTPUT / "product_summary.csv", index=False)

print(summary.to_string(index=False))
print("\nTop 5 products:")
print(top_products.head().to_string(index=False))
