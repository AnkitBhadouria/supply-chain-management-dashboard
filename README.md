# Supply Chain Management Dashboard Project

This project analyzes supply chain, transportation, delivery risk, sales, and customer/product performance using MySQL, Python validation logic, and Power BI.

## Project Objective

The objective is to convert supply chain data into a validated business intelligence dashboard that helps identify:

- Total shipment volume
- Late shipments
- On-time shipments
- High-risk shipments
- Average shipping days
- Delivery performance by region, route, shipping mode, and priority
- Sales and profit performance by product and customer segment

## Tools Used

- MySQL for data storage and SQL validation
- Python for optional validation checks
- Power BI for dashboard creation and visualization
- GitHub for project documentation and portfolio sharing

## Dashboard Pages

The Power BI report contains six completed pages:

1. Executive Overview
2. Transportation Performance
3. Route & Geographic Analysis
4. Sales & Customer Analysis
5. Delivery & Risk Analysis
6. Management & Operational Summary

## Key Dashboard Values

- Total Shipments: 180,519, displayed as 181K
- Late Shipments: 98,977, displayed as 99K
- On-Time Shipments: 32,226, displayed as 32K
- High-Risk Shipments: 98,977, displayed as 99K
- Average Shipping Days: 3.50
- Total Sales: 36,784,734.31
- Total Profit: 3,966,902.97
- Average Sales per Order: 559.45

## Repository Contents

```text
outputs/
  Supply_Chain_Management_Project_Finalization_Report.docx
  Supply_Chain_Management_Viva_Deck.pptx
  sql_validation_queries.sql
  python_validation_template.py
```

## Validation

Dashboard values should be validated using the SQL queries in:

```text
outputs/sql_validation_queries.sql
```

The Python validation template is included for CSV-based validation. If the data exists only inside MySQL, SQL validation is enough for the current version of the project.

## Main Business Insights

- Late shipments and high-risk shipments are a major operational concern.
- Standard Class has the highest shipment volume, so improvements in this shipping mode can have the largest impact.
- Some routes show 100% late shipment behavior and should be reviewed as high-risk routes.
- High-priority shipments should be investigated carefully because the current dashboard shows them as fully late/high-risk in the available data.
- Customer and product analysis connects logistics performance with sales and profit contribution.

## Future Scope

- Add delay forecasting.
- Add real-time shipment tracking.
- Include carrier cost and delivery cost analysis.
- Add root-cause delay fields such as warehouse delay, carrier delay, distance, and weather.
- Build automated refresh and monitoring.

## Project Status

Final dashboard documentation and viva presentation package are complete. The next step is to add actual Power BI screenshots to the presentation and upload the project to GitHub.
