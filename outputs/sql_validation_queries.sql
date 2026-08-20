-- Supply Chain Management Project - SQL Validation Queries
-- Replace table and column names if your MySQL schema uses different names.
-- Purpose: prove that Power BI KPI values match the database.

USE your_database_name;

-- 1. Total shipments
SELECT COUNT(*) AS total_shipments
FROM Transportation;

-- 2. Late shipments
SELECT COUNT(*) AS late_shipments
FROM Transportation
WHERE Delivery_Status = 'Late delivery';

-- 3. On-time shipments
SELECT COUNT(*) AS on_time_shipments
FROM Transportation
WHERE Delivery_Status = 'Shipping on time';

-- 4. Average shipping days
SELECT ROUND(AVG(Shipping_Days), 2) AS average_shipping_days
FROM Transportation;

-- 5. Shipment volume by shipping mode
SELECT
    Shipping_Mode,
    COUNT(*) AS total_shipments
FROM Transportation
GROUP BY Shipping_Mode
ORDER BY total_shipments DESC;

-- Expected known dashboard values:
-- Standard Class: 107752
-- Second Class: 35216
-- First Class: 27814
-- Same Day: 9737

-- 6. Shipment volume by region
SELECT
    Order_Region,
    COUNT(*) AS total_shipments
FROM Transportation
GROUP BY Order_Region
ORDER BY total_shipments DESC;

-- 7. Late shipment percentage by region
SELECT
    Order_Region,
    COUNT(*) AS total_shipments,
    SUM(CASE WHEN Delivery_Status = 'Late delivery' THEN 1 ELSE 0 END) AS late_shipments,
    ROUND(
        SUM(CASE WHEN Delivery_Status = 'Late delivery' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS late_shipment_percentage
FROM Transportation
GROUP BY Order_Region
ORDER BY late_shipment_percentage DESC;

-- 8. Priority performance
SELECT
    Priority,
    COUNT(*) AS total_shipments,
    SUM(CASE WHEN Delivery_Status = 'Late delivery' THEN 1 ELSE 0 END) AS late_shipments
FROM Transportation
GROUP BY Priority
ORDER BY total_shipments DESC;

-- 9. High-risk routes by late shipment percentage
SELECT
    Origin_Location,
    Destination_Location,
    COUNT(*) AS total_shipments,
    SUM(CASE WHEN Delivery_Status = 'Late delivery' THEN 1 ELSE 0 END) AS late_shipments,
    ROUND(
        SUM(CASE WHEN Delivery_Status = 'Late delivery' THEN 1 ELSE 0 END) * 1.0 / COUNT(*),
        2
    ) AS route_late_percentage
FROM Transportation
GROUP BY Origin_Location, Destination_Location
HAVING route_late_percentage >= 0.70
ORDER BY route_late_percentage DESC, total_shipments DESC;

-- 10. Customer segment totals
SELECT
    Customer_Segment,
    COUNT(*) AS total_shipments,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(AVG(Sales), 2) AS average_sales_per_order
FROM Product
GROUP BY Customer_Segment
ORDER BY total_sales DESC;

-- Expected known dashboard values:
-- Consumer: 93504 shipments, 19.10M sales, 2.07M profit
-- Corporate: 54789 shipments, 11.17M sales, 1.20M profit
-- Home Office: 32226 shipments, 6.52M sales, 0.69M profit

-- 11. Total sales, profit, and average sales per order
SELECT
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(AVG(Sales), 2) AS average_sales_per_order
FROM Product;

-- Expected known dashboard values:
-- Total Sales: 36784734.31
-- Total Profit: 3966902.97
-- Average Sales per Order: 559.45
