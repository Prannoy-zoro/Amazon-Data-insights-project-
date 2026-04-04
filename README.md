# Amazon Data Insights Dashboard

This project is an end-to-end data analysis and visualization application built using Python. It focuses on exploring an Amazon products dataset to understand pricing patterns, discount behavior, and customer ratings through an interactive dashboard.

---

## Project Overview

The objective of this project was to work with a real-world dataset and build a structured workflow that includes data cleaning, feature engineering, and visualization.

The dashboard allows users to explore the dataset interactively and gain insights into how different product categories perform in terms of pricing, discounts, and ratings.

---

## Key Features

- Data cleaning and preprocessing:
  - Removed currency symbols and formatting inconsistencies
  - Converted relevant columns into numeric data types
  - Handled missing values and removed invalid entries
  - Eliminated duplicate records

- Feature engineering:
  - Created a new column `savings` to represent the difference between actual price and discounted price

- Interactive visualizations:
  - Category vs average rating
  - Rating vs discounted price
  - Discount percentage distribution
  - Category distribution using pie charts
  - Additional exploratory plots for deeper analysis

- User interaction:
  - Filters for category, price range, and minimum rating
  - Dynamic updates across all visualizations based on selected filters

---

## Technology Stack

- Python
- Pandas
- Plotly
- Streamlit

---

## Dataset

The dataset consists of Amazon product listings with approximately 1400 entries. It includes information such as product name, category, pricing details, ratings, and review counts.

---

## Key Learnings

- Handling and cleaning real-world datasets with inconsistent formatting
- Converting string-based data into usable numerical formats
- Creating derived features to improve analysis quality
- Designing and structuring an interactive dashboard
- Understanding how to present data insights clearly through visualization

---


