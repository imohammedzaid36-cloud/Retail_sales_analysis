

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# STEP 1: LOAD DATASET
# ============================================================

df = pd.read_csv("data/Sample - Superstore.csv", encoding="cp1252")
print("DATASET LOADED SUCCESSFULLY!")

# ============================================================
# STEP 2: DISPLAY FIRST 5 ROWS
# ============================================================

print("\nFIRST 5 ROWS:")
print(df.head())

# ============================================================
# STEP 3: DATASET INFORMATION
# ============================================================

print("\nDATASET INFORMATION:")
print(df.info())

# ============================================================
# STEP 4: DATASET SHAPE
# ============================================================

print("\nDATASET SHAPE:")
print(df.shape)

# ============================================================
# STEP 5: CHECK MISSING VALUES
# ============================================================

print("\nMISSING VALUES:")
print(df.isnull().sum())

# ============================================================
# STEP 6: CHECK DUPLICATE ROWS
# ============================================================

print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

# ============================================================
# STEP 7: CONVERT DATE COLUMNS
# ============================================================

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("\nDATE COLUMNS CONVERTED SUCCESSFULLY!")

# ============================================================
# STEP 8: OVERALL SALES, PROFIT AND QUANTITY
# ============================================================

print("\nTOTAL SALES:")
print(round(df["Sales"].sum(), 2))

print("\nTOTAL PROFIT:")
print(round(df["Profit"].sum(), 2))

print("\nTOTAL QUANTITY SOLD:")
print(df["Quantity"].sum())

# ============================================================
# STEP 9: SALES BY CATEGORY
# ============================================================

category_sales = df.groupby("Category")["Sales"].sum()

print("\nSALES BY CATEGORY:")
print(category_sales)

# ============================================================
# STEP 10: SALES BY REGION
# ============================================================

region_sales = df.groupby("Region")["Sales"].sum()

print("\nSALES BY REGION:")
print(region_sales)

# ============================================================
# STEP 11: PROFIT BY CATEGORY
# ============================================================

category_profit = df.groupby("Category")["Profit"].sum()

print("\nPROFIT BY CATEGORY:")
print(category_profit)

# ============================================================
# STEP 12: SALES AND PROFIT BY REGION
# ============================================================

region_analysis = df.groupby("Region")[["Sales", "Profit"]].sum()

print("\nSALES AND PROFIT BY REGION:")
print(region_analysis)

# ============================================================
# STEP 13: SALES AND PROFIT BY SUB-CATEGORY
# ============================================================

subcategory_analysis = df.groupby("Sub-Category")[
    ["Sales", "Profit"]
].sum()

subcategory_analysis = subcategory_analysis.sort_values(
    by="Sales", ascending=False
)

print("\nSALES AND PROFIT BY SUB-CATEGORY:")
print(subcategory_analysis)

# ============================================================
# STEP 14: SALES BY CUSTOMER SEGMENT
# ============================================================

segment_sales = df.groupby("Segment")["Sales"].sum()

print("\nSALES BY CUSTOMER SEGMENT:")
print(segment_sales)

# ============================================================
# STEP 15: PROFIT BY CUSTOMER SEGMENT
# ============================================================

segment_profit = df.groupby("Segment")["Profit"].sum()

print("\nPROFIT BY CUSTOMER SEGMENT:")
print(segment_profit)

# ============================================================
# STEP 16: TOP 10 CUSTOMERS BY SALES
# ============================================================

customer_sales = df.groupby("Customer Name")["Sales"].sum()

top_10_customers = customer_sales.sort_values(
    ascending=False
).head(10)

print("\nTOP 10 CUSTOMERS BY SALES:")
print(top_10_customers)

# ============================================================
# STEP 17: CATEGORY SALES CHART
# ============================================================

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales ($)")
plt.tight_layout()
plt.savefig("category_sales.png", dpi=300)
plt.show()

# ============================================================
# STEP 18: REGION SALES CHART
# ============================================================

plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales ($)")
plt.tight_layout()
plt.savefig("region_sales.png", dpi=300)
plt.show()

# ============================================================
# STEP 19: CATEGORY PROFIT CHART
# ============================================================

plt.figure(figsize=(8, 5))
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit ($)")
plt.tight_layout()
plt.savefig("category_profit.png", dpi=300)
plt.show()

# ============================================================
# STEP 20: SALES AND PROFIT BY REGION CHART
# ============================================================

region_analysis.plot(kind="bar", figsize=(9, 5))
plt.title("Sales and Profit by Region")
plt.xlabel("Region")
plt.ylabel("Amount ($)")
plt.tight_layout()
plt.savefig("region_sales_profit.png", dpi=300)
plt.show()

# ============================================================
# STEP 21: SUB-CATEGORY SALES CHART
# ============================================================

plt.figure(figsize=(12, 6))
subcategory_analysis["Sales"].sort_values().plot(kind="barh")
plt.title("Sales by Sub-Category")
plt.xlabel("Total Sales ($)")
plt.ylabel("Sub-Category")
plt.tight_layout()
plt.savefig("subcategory_sales.png", dpi=300)
plt.show()

# ============================================================
# STEP 22: CUSTOMER SEGMENT SALES CHART
# ============================================================

plt.figure(figsize=(8, 5))
segment_sales.plot(kind="bar")
plt.title("Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Sales ($)")
plt.tight_layout()
plt.savefig("segment_sales.png", dpi=300)
plt.show()

# ============================================================
# STEP 23: TOP 10 CUSTOMERS CHART
# ============================================================

plt.figure(figsize=(12, 6))
top_10_customers.sort_values().plot(kind="barh")
plt.title("Top 10 Customers by Sales")
plt.xlabel("Total Sales ($)")
plt.ylabel("Customer Name")
plt.tight_layout()
plt.savefig("top_10_customers.png", dpi=300)
plt.show()

# ============================================================
# STEP 24: MONTHLY SALES ANALYSIS
# ============================================================

df["Year-Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Year-Month")["Sales"].sum()

print("\nMONTHLY SALES:")
print(monthly_sales)

# ============================================================
# STEP 25: HIGHEST SALES MONTH
# ============================================================

highest_sales_month = monthly_sales.idxmax()

print("\nHIGHEST SALES MONTH:")
print(highest_sales_month)

print("TOTAL SALES:")
print(round(monthly_sales.max(), 2))

# ============================================================
# STEP 26: MONTHLY SALES CHART
# ============================================================

plt.figure(figsize=(14, 6))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales.png", dpi=300)
plt.show()

# ============================================================
# STEP 27: YEARLY SALES ANALYSIS
# ============================================================

df["Year"] = df["Order Date"].dt.year

yearly_sales = df.groupby("Year")["Sales"].sum()

print("\nYEARLY SALES:")
print(yearly_sales)

# ============================================================
# STEP 28: YEARLY PROFIT ANALYSIS
# ============================================================

yearly_profit = df.groupby("Year")["Profit"].sum()

print("\nYEARLY PROFIT:")
print(yearly_profit)

print("\nBEST SALES YEAR:")
print(yearly_sales.idxmax())

print("HIGHEST SALES:")
print(round(yearly_sales.max(), 2))

# ============================================================
# STEP 29: YEARLY SALES CHART
# ============================================================

plt.figure(figsize=(8, 5))
yearly_sales.plot(kind="bar")
plt.title("Yearly Sales")
plt.xlabel("Year")
plt.ylabel("Total Sales ($)")
plt.tight_layout()
plt.savefig("yearly_sales.png", dpi=300)
plt.show()

# ============================================================
# STEP 30: AVERAGE DISCOUNT BY CATEGORY
# ============================================================

average_discount = df.groupby("Category")["Discount"].mean() * 100

print("\nAVERAGE DISCOUNT BY CATEGORY:")
print(average_discount.round(2))

# ============================================================
# STEP 31: DISCOUNT ANALYSIS
# ============================================================

discount_analysis = df.groupby("Discount").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Average_Profit=("Profit", "mean"),
    Number_of_Orders=("Order ID", "count")
)

print("\nDISCOUNT ANALYSIS:")
print(discount_analysis.round(2))

highest_loss_discount = discount_analysis["Total_Profit"].idxmin()

print("\nDISCOUNT LEVEL WITH HIGHEST LOSS:")
print(highest_loss_discount * 100, "%")

print("TOTAL LOSS AT THIS DISCOUNT:")
print(round(discount_analysis.loc[highest_loss_discount, "Total_Profit"], 2))

# ============================================================
# STEP 32: DISCOUNT AND PROFIT CHART
# ============================================================

plt.figure(figsize=(10, 5))
discount_analysis["Total_Profit"].plot(kind="bar")
plt.title("Profit by Discount Level")
plt.xlabel("Discount")
plt.ylabel("Total Profit ($)")
plt.tight_layout()
plt.savefig("discount_profit.png", dpi=300)
plt.show()

# ============================================================
# STEP 33: SHIPPING MODE ANALYSIS
# ============================================================

shipping_analysis = df.groupby("Ship Mode").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Number_of_Orders=("Order ID", "count")
)

print("\nSHIPPING MODE ANALYSIS:")
print(shipping_analysis.round(2))

print("\nMOST POPULAR SHIPPING MODE:")
print(shipping_analysis["Number_of_Orders"].idxmax())

# ============================================================
# STEP 34: DELIVERY TIME ANALYSIS
# ============================================================

df["Delivery Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

delivery_analysis = df.groupby("Ship Mode")["Delivery Days"].mean()

print("\nAVERAGE DELIVERY DAYS BY SHIPPING MODE:")
print(delivery_analysis.round(2))

print("\nFASTEST SHIPPING MODE:")
print(delivery_analysis.idxmin())

print("AVERAGE DELIVERY DAYS:")
print(round(delivery_analysis.min(), 2))

# ============================================================
# STEP 35: PRODUCT SALES AND PROFIT ANALYSIS
# ============================================================

product_analysis = df.groupby("Product Name").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
)

top_10_products_sales = product_analysis.sort_values(
    by="Sales", ascending=False
).head(10)

print("\nTOP 10 PRODUCTS BY SALES:")
print(top_10_products_sales["Sales"])

top_10_products_profit = product_analysis.sort_values(
    by="Profit", ascending=False
).head(10)

print("\nTOP 10 PRODUCTS BY PROFIT:")
print(top_10_products_profit["Profit"])

# ============================================================
# STEP 36: LOSS-MAKING PRODUCT ANALYSIS
# ============================================================

loss_products = product_analysis[product_analysis["Profit"] < 0]

print("\nNUMBER OF LOSS-MAKING PRODUCTS:")
print(len(loss_products))

top_10_loss_products = loss_products.sort_values(
    by="Profit", ascending=True
).head(10)

print("\nTOP 10 PRODUCTS WITH HIGHEST LOSSES:")
print(top_10_loss_products["Profit"])

best_selling_product = product_analysis["Sales"].idxmax()

print("\nBEST-SELLING PRODUCT:")
print(best_selling_product)

print("TOTAL SALES:")
print(round(product_analysis.loc[best_selling_product, "Sales"], 2))

# ============================================================
# STEP 37: STATE AND CITY PERFORMANCE ANALYSIS
# ============================================================

state_analysis = df.groupby("State").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

top_10_states = state_analysis.sort_values(
    by="Total_Sales", ascending=False
).head(10)

print("\nTOP 10 STATES BY SALES:")
print(top_10_states.round(2))

most_profitable_state = state_analysis["Total_Profit"].idxmax()

print("\nMOST PROFITABLE STATE:")
print(most_profitable_state)

print("TOTAL PROFIT:")
print(round(state_analysis.loc[most_profitable_state, "Total_Profit"], 2))

least_profitable_state = state_analysis["Total_Profit"].idxmin()

print("\nLEAST PROFITABLE STATE:")
print(least_profitable_state)

print("TOTAL PROFIT:")
print(round(state_analysis.loc[least_profitable_state, "Total_Profit"], 2))

city_analysis = df.groupby("City").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

top_10_cities = city_analysis.sort_values(
    by="Total_Sales", ascending=False
).head(10)

print("\nTOP 10 CITIES BY SALES:")
print(top_10_cities.round(2))

best_city = city_analysis["Total_Sales"].idxmax()

print("\nBEST-PERFORMING CITY BY SALES:")
print(best_city)

print("TOTAL SALES:")
print(round(city_analysis.loc[best_city, "Total_Sales"], 2))

most_profitable_city = city_analysis["Total_Profit"].idxmax()

print("\nMOST PROFITABLE CITY:")
print(most_profitable_city)

print("TOTAL PROFIT:")
print(round(city_analysis.loc[most_profitable_city, "Total_Profit"], 2))

# State sales chart
plt.figure(figsize=(12, 6))
top_10_states["Total_Sales"].sort_values().plot(kind="barh")
plt.title("Top 10 States by Sales")
plt.xlabel("Total Sales ($)")
plt.ylabel("State")
plt.tight_layout()
plt.savefig("top_10_states_sales.png", dpi=300)
plt.show()

# City sales chart
plt.figure(figsize=(12, 6))
top_10_cities["Total_Sales"].sort_values().plot(kind="barh")
plt.title("Top 10 Cities by Sales")
plt.xlabel("Total Sales ($)")
plt.ylabel("City")
plt.tight_layout()
plt.savefig("top_10_cities_sales.png", dpi=300)
plt.show()

# ============================================================
# STEP 38: CORRELATION ANALYSIS
# ============================================================

correlation_data = df[
    ["Sales", "Profit", "Quantity", "Discount"]
]

correlation_matrix = correlation_data.corr()

print("\nCORRELATION BETWEEN SALES, PROFIT, QUANTITY AND DISCOUNT:")
print(correlation_matrix.round(3))

# Sales and Profit relationship
print("\nSALES AND PROFIT CORRELATION:")
print(round(correlation_matrix.loc["Sales", "Profit"], 3))

# Discount and Profit relationship
print("\nDISCOUNT AND PROFIT CORRELATION:")
print(round(correlation_matrix.loc["Discount", "Profit"], 3))

# Quantity and Sales relationship
print("\nQUANTITY AND SALES CORRELATION:")
print(round(correlation_matrix.loc["Quantity", "Sales"], 3))

# Correlation heatmap
plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=300)
plt.show()

print("\nALL ANALYSIS COMPLETED SUCCESSFULLY!")


