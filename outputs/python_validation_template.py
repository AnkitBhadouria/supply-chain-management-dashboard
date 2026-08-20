"""
Supply Chain Management Project - Python Validation Template

Update TRANSPORTATION_CSV and PRODUCT_CSV to match your local file names.
Run this script before final submission to create independent validation
evidence for your Power BI dashboard.
"""

from pathlib import Path

import pandas as pd


TRANSPORTATION_CSV = Path("Transportation.csv")
PRODUCT_CSV = Path("Product.csv")


def print_section(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def load_csv(path):
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path.resolve()}")
    return pd.read_csv(path)


def basic_checks(name, df):
    print_section(f"{name} - Basic Checks")
    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nData types:")
    print(df.dtypes)
    print("\nMissing values:")
    print(df.isna().sum().sort_values(ascending=False))
    print("\nDuplicate rows:", df.duplicated().sum())


def transportation_kpis(df):
    print_section("Transportation KPI Validation")

    total_shipments = len(df)
    late_shipments = (df["Delivery_Status"] == "Late delivery").sum()
    on_time_shipments = (df["Delivery_Status"] == "Shipping on time").sum()

    print("Total Shipments:", total_shipments)
    print("Late Shipments:", late_shipments)
    print("On Time Shipments:", on_time_shipments)

    if "Shipping_Days" in df.columns:
        print("Average Shipping Days:", round(df["Shipping_Days"].mean(), 2))

    print("\nShipment Volume by Shipping Mode:")
    print(df["Shipping_Mode"].value_counts())

    print("\nShipment Volume by Region:")
    print(df["Order_Region"].value_counts())

    print("\nPriority Performance:")
    print(df.groupby("Priority").size().sort_values(ascending=False))

    print("\nLate Shipment % by Region:")
    region_summary = (
        df.assign(Is_Late=df["Delivery_Status"].eq("Late delivery"))
        .groupby("Order_Region")
        .agg(total_shipments=("Delivery_Status", "size"), late_shipments=("Is_Late", "sum"))
    )
    region_summary["late_shipment_percentage"] = (
        region_summary["late_shipments"] / region_summary["total_shipments"] * 100
    ).round(2)
    print(region_summary.sort_values("late_shipment_percentage", ascending=False))

    print("\nHigh-Risk Routes - Highest Late Shipment %:")
    route_summary = (
        df.assign(Is_Late=df["Delivery_Status"].eq("Late delivery"))
        .groupby(["Origin_Location", "Destination_Location"])
        .agg(total_shipments=("Delivery_Status", "size"), late_shipments=("Is_Late", "sum"))
    )
    route_summary["route_late_percentage"] = (
        route_summary["late_shipments"] / route_summary["total_shipments"]
    ).round(2)
    print(
        route_summary[route_summary["route_late_percentage"] >= 0.70]
        .sort_values(["route_late_percentage", "total_shipments"], ascending=[False, False])
        .head(20)
    )


def product_kpis(df):
    print_section("Product / Sales KPI Validation")

    print("Total Sales:", round(df["Sales"].sum(), 2))
    print("Total Profit:", round(df["Profit"].sum(), 2))
    print("Average Sales per Order:", round(df["Sales"].mean(), 2))

    print("\nCustomer Segment Performance:")
    segment_summary = (
        df.groupby("Customer_Segment")
        .agg(
            total_sales=("Sales", "sum"),
            total_shipments=("Customer_Segment", "size"),
            total_profit=("Profit", "sum"),
            average_sales_per_order=("Sales", "mean"),
        )
        .round(2)
        .sort_values("total_sales", ascending=False)
    )
    print(segment_summary)

    if "Product_Category" in df.columns:
        print("\nSales by Product Category:")
        print(df.groupby("Product_Category")["Sales"].sum().round(2).sort_values(ascending=False))

    if "Product_Name" in df.columns:
        print("\nTop 10 Products by Sales:")
        print(df.groupby("Product_Name")["Sales"].sum().round(2).sort_values(ascending=False).head(10))

        print("\nTop 10 Products by Profit:")
        print(df.groupby("Product_Name")["Profit"].sum().round(2).sort_values(ascending=False).head(10))


def main():
    transportation = load_csv(TRANSPORTATION_CSV)
    product = load_csv(PRODUCT_CSV)

    basic_checks("Transportation", transportation)
    basic_checks("Product", product)
    transportation_kpis(transportation)
    product_kpis(product)


if __name__ == "__main__":
    main()
