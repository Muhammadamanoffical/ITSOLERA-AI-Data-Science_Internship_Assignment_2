import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="🌟 Global Superstore Dashboard", layout="wide")
st.title("📊 Global Superstore Business Dashboard")

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("superstore_cleaned.csv")
df["Order.Date"] = pd.to_datetime(df["Order.Date"])

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filters")

region_filter = st.sidebar.multiselect(
    "Select Region:",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category_filter = st.sidebar.multiselect(
    "Select Category:",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

sub_category_filter = st.sidebar.multiselect(
    "Select Sub-Category:",
    options=df["Sub.Category"].unique(),
    default=df["Sub.Category"].unique()
)

# Apply Filters
filtered_df = df[
    (df["Region"].isin(region_filter)) &
    (df["Category"].isin(category_filter)) &
    (df["Sub.Category"].isin(sub_category_filter))
]

# -----------------------------
# KPI Section
# -----------------------------
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()

top_customers = (
    filtered_df.groupby("Customer.Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

col1, col2 = st.columns(2)
col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("📈 Total Profit", f"${total_profit:,.2f}")

st.subheader("🏆 Top 5 Customers by Sales")
st.dataframe(top_customers)

# -----------------------------
# Charts
# -----------------------------
# Sales by Category
st.subheader("Sales by Category")
sales_cat = filtered_df.groupby("Category")["Sales"].sum().reset_index()
fig1 = px.bar(
    sales_cat,
    x="Category",
    y="Sales",
    color="Category",
    text="Sales",
    title="Total Sales by Category"
)
st.plotly_chart(fig1, use_container_width=True)

# Profit by Region
st.subheader("Profit by Region")
profit_region = filtered_df.groupby("Region")["Profit"].sum().reset_index()
fig2 = px.bar(
    profit_region,
    x="Region",
    y="Profit",
    color="Region",
    text="Profit",
    title="Total Profit by Region"
)
st.plotly_chart(fig2, use_container_width=True)

# Optional: Sales Trend Over Time
st.subheader("Sales Trend Over Time")
sales_trend = filtered_df.groupby("Order.Date")["Sales"].sum().reset_index()
fig3 = px.line(
    sales_trend,
    x="Order.Date",
    y="Sales",
    title="Sales Trend Over Time"
)
st.plotly_chart(fig3, use_container_width=True)

# Optional: Profit by Sub-Category Pie Chart
st.subheader("Profit by Sub-Category")
profit_sub = filtered_df.groupby("Sub.Category")["Profit"].sum().reset_index()
fig4 = px.pie(
    profit_sub,
    values="Profit",
    names="Sub.Category",
    title="Profit Distribution by Sub-Category"
)
st.plotly_chart(fig4, use_container_width=True)