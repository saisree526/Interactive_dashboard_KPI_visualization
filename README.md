# 📊 Interactive Business Dashboard & KPI Visualizations

## 📌 Project Overview

The **Interactive Business Dashboard & KPI Visualizations** project focuses on analyzing business performance using Power BI. It transforms sales and customer data into interactive visualizations that help users understand revenue trends, profitability, customer behavior, and business performance.

The dashboard includes key performance indicators (KPIs), charts, and filters to support data-driven decision-making.

## 🎯 Objectives

- Analyze total revenue and profit.
- Track order volume and customer count.
- Calculate Average Order Value (AOV).
- Visualize monthly revenue trends.
- Compare revenue across regions and product categories.
- Understand Customer Acquisition Cost (CAC).
- Analyze customer churn rate using additional practice data.

## 🛠️ Tools and Technologies

- **Power BI Desktop** – Dashboard development and visualization.
- **Microsoft Excel** – Additional KPI practice data.
- **CSV Dataset** – Superstore sales data.
- **Power Query** – Data cleaning and transformation.
- **DAX** – Calculated measures and KPI calculations.

## 📂 Project Files

```text
Interactive-Business-Dashboard/
│
├── clean_superstore.csv
├── cac_churn_practice_metrics.xlsx
├── README.md
└── Business_Performance_Dashboard.pbix
```

*Note: The `.pbix` file is the Power BI report. Include it in the repository after saving your dashboard.*

## 📈 Key Performance Indicators (KPIs)

| KPI | Description |
|---|---|
| Total Revenue | Total sales revenue generated |
| Total Profit | Total profit earned |
| Total Orders | Number of unique orders |
| Total Customers | Number of unique customers |
| Average Order Value (AOV) | Average revenue per order |
| Customer Acquisition Cost (CAC) | Marketing spend divided by new customers acquired |
| Customer Churn Rate | Percentage of customers lost during a period |

## 📊 Dashboard Visualizations

- **KPI Cards:** Total Revenue, Total Profit, Orders, Customers, AOV, CAC, and Churn Rate.
- **Monthly Revenue Trend:** Displays revenue changes over time.
- **Revenue by Region:** Compares revenue across geographical regions.
- **Sales by Product Category:** Identifies categories contributing to sales.
- **Revenue by City:** Displays geographical sales distribution.
- **Interactive Filters:** Enables analysis by date, region, category, and other available fields.

## 🧮 KPI Formulas

### Average Order Value

```text
Average Order Value = Total Revenue / Total Orders
```

### Customer Acquisition Cost

```text
CAC = Total Marketing Spend / New Customers Acquired
```

### Customer Churn Rate

```text
Churn Rate = (Customers Lost / Starting Customers) × 100
```

**Important:** The Superstore dataset does not contain the marketing spend and customer lifecycle information required to calculate CAC and churn rate. The supplementary Excel workbook contains synthetic practice data for learning and demonstrating these KPIs. These metrics should not be presented as actual Superstore business results.

## 🚀 How to Run the Project

1. Install and open Power BI Desktop.
2. Import `clean_superstore.csv` using **Home → Get Data → Text/CSV**.
3. Load the dataset and verify the data types in Power Query.
4. Import `cac_churn_practice_metrics.xlsx` using **Home → Get Data → Excel Workbook**.
5. Select the `CustomerMetrics` sheet and load it.
6. Create DAX measures for the required KPIs.
7. Add card visuals, charts, and slicers to the report canvas.
8. Format the report with suitable titles, labels, and consistent colors.
9. Save the report as `Business_Performance_Dashboard.pbix`.

## 💡 Business Benefits

- Provides a clear overview of business performance.
- Helps identify profitable product categories and regions.
- Makes revenue trends easier to understand.
- Supports customer acquisition and retention analysis.
- Improves reporting efficiency through interactive visualizations.
- Helps users make informed, data-driven decisions.

## 🔮 Future Enhancements

- Connect the dashboard to a live database.
- Add year-over-year and month-over-month comparisons.
- Include customer segmentation and retention analysis.
- Add automated data refresh.
- Publish the report to Power BI Service, subject to account and workspace permissions.

## 👩‍💻 Project Type

**Domain:** Data Analytics and Business Intelligence  
**Level:** Student Project  
**Primary Tool:** Microsoft Power BI  
**Skills Demonstrated:** Data Cleaning, Data Visualization, DAX, KPI Analysis, Business Intelligence, and Dashboard Design.

## 📌 Conclusion

This project demonstrates how raw business data can be transformed into an interactive dashboard for monitoring KPIs and analyzing business performance. It provides practical experience in data preparation, DAX calculations, and business intelligence reporting.
