# mai-shan-yun_Datathon

## Overview
This project presents an **interactive inventory management dashboard** for a restaurant, designed to help managers track ingredient consumption, monitor stock levels, and make data-driven decisions. The dashboard integrates multiple datasets and provides insights into menu-item sales, ingredient usage, seasonal trends, and predictive analytics.

---

## Datasets Used
1. **Item Sales Data** (`May` ~ `November`)  
   - Contains `Item Name`, `Count`, `Amount`, `Month`, `Month_Label`.
   - Used to calculate ingredient consumption per menu item.

2. **Ingredient Mapping** (`MSY Data - Ingredient`)  
   - Maps each menu item to its ingredients and their quantities.
   - Allows computation of ingredient-level usage.

3. **Shipment Data** (`MSY Data - Shipment`)  
   - Provides shipment frequency, quantity, and units per ingredient.
   - Used to calculate total stock received.

---
## Data Table Relationships

<img width="741" height="241" alt="截圖 2025-11-09 凌晨4 12 42" src="https://github.com/user-attachments/assets/b4e3250c-7208-4591-b005-f89c35525da3" />

---
## Dashboard Features

### 1. Inventory & Stock Analysis
- **Current Stock vs. Consumption**: Calculates current stock based on shipments and consumption.  
- **Stock Status**: Flags ingredients as *Low Stock*, *Normal*, or *Overstock*.  
- **Visualization**: Heat maps, bar charts, and KPI tables show inventory status per ingredient over time.

### 2. Ingredient Insights
- Tracks **Top-Used** and **Least-Used** ingredients monthly.  
- Provides ranking tables and interactive bar charts for deeper insight.

### 3. Menu-to-Ingredient Interaction
- Clicking on a **menu item** dynamically filters the dashboard to show its impact on ingredient usage over time.  
- Helps managers understand which menu items drive specific ingredient consumption.

### 4. Predictive Analytics
- Forecasts future ingredient needs based on historical menu item sales.  
- Helps anticipate reorder timing and potential stock shortages.

### 5. Shipment Tracking
- Visualizes shipment frequency and quantity per ingredient.  
- Highlights patterns in deliveries and potential delays.

---

## Evaluation Alignment

### Creativity & Insight (50%)
- **Innovative Visualization**: Interactive heat maps, line charts, and ranking tables make insights clear and engaging.  
- **Smart Analytics**: Trends in ingredient consumption, seasonal patterns, and predictive forecasts are uncovered.  
- **Actionability**: Dashboard empowers decision-making with reorder alerts, stock status flags, and ingredient forecasting.

### Technical Merit & Utility (50%)
- **Functionality**: All dashboards pull insights directly from the integrated datasets and respond to user interactions.  
- **Data Handling**: Data is cleaned, merged, and transformed efficiently to calculate ingredient-level consumption and stock.  
- **Usability**: Dashboard is intuitive, with clear labeling, filters, and drill-down functionality.  
- **Performance**: Handles multiple months of data with smooth interactivity and minimal lag.

---

## How to Use
1. Open the Tableau dashboard file `mai-shan-yun_Datathon.twbx`.  
2. Explore **Menu Sales**, **Ingredient Consumption**, and **Stock Status** sheets.  
3. Click on a menu item to filter ingredient consumption and forecast trends.  
4. Adjust **Threshold Parameters** for low stock or overstock alerts.  
5. Use the dashboard filters to explore specific months, ingredients, or categories.

---

## Conclusion
This dashboard integrates sales, ingredient, and shipment data to provide a **comprehensive view of restaurant inventory management**, enabling managers to make proactive decisions, optimize costs, and ensure smooth operations.
