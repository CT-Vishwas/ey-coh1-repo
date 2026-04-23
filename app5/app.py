import os
from pathlib import Path

import streamlit as st

from src.data_processing import load_csv, describe_data, filter_columns, get_unique_values
from src.reporting import build_report, save_report
from src.utils.file_io import ensure_dir
import pandas as pd

REPORT_DIR = Path("reports")


def render_header() -> None:
    st.set_page_config(page_title="CSV Processor & Report Generator", layout="wide")
    st.title("CSV Processor & Report Generator")
    st.markdown(
        "Upload a CSV file, inspect the data, and generate a reusable summary report in CSV or JSON format."
    )


def render_sidebar(df: pd.DataFrame) -> str:
    st.sidebar.header("Report settings")
    report_format = st.sidebar.selectbox("Report format", ["CSV", "JSON"])
    # Dropdown to filter profits by category and subcategory, full stretch
    st.sidebar.subheader("Filter by Category")
    category_filter = st.sidebar.multiselect("Select categories to include in the report", options=[category for category in get_unique_values(df, 'Category') if category is not None])
    st.sidebar.subheader("Filter by Sub Category")
    subcategory_filter = st.sidebar.multiselect("Select subcategories to include in the report", options=[subcategory for subcategory in get_unique_values(df, 'Sub Category') if subcategory is not None])
    return report_format


def main() -> None:

    csv_path = Path("data/Retail Analytics Dataset.csv")
    if not csv_path.exists():
        st.error("CSV file not found in data folder. Please ensure 'Retail Analytics Dataset.csv' is present.")
        return

    df = load_csv(csv_path)

    render_header()
    report_format = render_sidebar(df)

    # Calculate KPIs
    total_sales = df['Sales'].sum() if 'Sales' in df.columns else None
    total_profit = df['Profit'].sum() if 'Profit' in df.columns else None
    total_quantity = df['Quantity'].sum() if 'Quantity' in df.columns else None

    # Display KPIs in 3 columns for full stretch
    col1, col2, col3 = st.columns(3)
    with col1:
        if total_sales is not None:
            st.metric("Total Sales", f"${total_sales:,.2f}")
    with col2:
        if total_profit is not None:
            st.metric("Total Profit", f"${total_profit:,.2f}")
    with col3:
        if total_quantity is not None:
            st.metric("Total Quantity Sold", total_quantity)

    st.subheader("Profits")
    # two columns for profit by category and profit by subcategory, full stretch
    col1, col2 = st.columns(2)
    with col1:
        if 'Category' in df.columns and 'Profit' in df.columns:
            profit_by_category = df.groupby('Category')['Profit'].sum().reset_index()
            st.bar_chart(profit_by_category.set_index('Category'))
    with col2:
        if 'Sub Category' in df.columns and 'Profit' in df.columns:
            profit_by_subcategory = df.groupby('Sub Category')['Profit'].sum().reset_index()
            st.bar_chart(profit_by_subcategory.set_index('Sub Category'))

if __name__ == "__main__":
    main()
