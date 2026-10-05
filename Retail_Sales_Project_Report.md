# Real-World Data Project: Retail Sales Analysis

## 1. Introduction
This project applies data-analysis techniques to a retail sales dataset. The goal is to identify sales patterns, profitable product categories, strong regions, customer payment preferences, and top-performing products.

## 2. Dataset
The dataset contains **1,200 retail transactions** from **January to December 2025**. Each record includes order date, customer ID, region, category, product, quantity, unit price, discount, payment method, sales, cost, and profit.

The dataset is synthetic and was created specifically for educational use.

## 3. Key Performance Indicators

| KPI | Result |
|---|---:|
| Total Sales | ₹3,393,361.81 |
| Total Profit | ₹1,039,314.65 |
| Orders | 1,200 |
| Average Order Value | ₹2,827.80 |
| Profit Margin | 30.63% |

## 4. Analysis and Visualizations

### Monthly sales trend
![Monthly Sales](charts/01_monthly_sales.png)

Sales vary throughout the year, with **2025-05** recording the highest monthly sales in this dataset.

### Category performance
![Category Sales](charts/02_category_sales.png)

**Electronics** is the highest-sales category. Category-level analysis can help management prioritize inventory and promotional budgets.

### Regional performance
![Regional Sales](charts/03_region_sales.png)

**South** is the strongest region by sales. Regional performance should be monitored to identify opportunities for expansion or targeted campaigns.

### Payment methods
![Payment Sales](charts/04_payment_sales.png)

Digital payment methods account for a substantial share of transactions, indicating the importance of maintaining convenient digital checkout options.

### Top products
![Top Products](charts/05_top_products.png)

**Smart Watch** is the highest-selling product in the dataset. The top products should receive careful stock-level monitoring to reduce the risk of stock-outs.

### Profitability by category
![Category Profit](charts/06_category_profit.png)

Sales volume alone should not determine business priorities. Profit by category provides an additional view of which product groups contribute most to earnings.

## 5. Findings
1. **Category:** Electronics leads total sales.
2. **Region:** South generates the highest regional sales.
3. **Product:** Smart Watch is the top product by sales.
4. **Time:** 2025-05 is the strongest month in the dataset.
5. **Profitability:** The overall profit margin is approximately **30.63%**.
6. **Operations:** High-performing products and categories should receive stronger inventory planning.

## 6. Business Recommendations
- Maintain sufficient inventory for high-performing products.
- Use category-level profit, not just sales, when planning promotions.
- Focus marketing experiments on the strongest region while testing growth campaigns in weaker regions.
- Encourage digital payment options because of their convenience and broad adoption.
- Review discount levels to ensure that additional sales are generating sufficient profit.
- Repeat this analysis monthly so management can detect changes early.

## 7. Conclusion
The project demonstrates an end-to-end retail analytics workflow: data preparation, KPI calculation, aggregation, visualization, interpretation, and business recommendations. The analysis shows how basic data-science techniques can turn transaction data into practical business insights.
