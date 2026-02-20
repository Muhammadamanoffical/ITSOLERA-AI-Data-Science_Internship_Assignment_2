# IT Solera PVT LTD - AI & Data Science Internship Assignment 2

## Intern: Muhammad Aman
**GitHub:** [https://github.com/Muhammadamanoffical](https://github.com/Muhammadamanoffical)

---

## Overview
This repository contains the **Advanced Internship Tasks** for the AI & Data Science Internship at IT Solera PVT LTD.  
All tasks are completed as per the internship guidelines, with well-structured Jupyter Notebooks, visualizations, and insights.

**Completed Tasks:**
1. Term Deposit Subscription Prediction (Bank Marketing)
2. Customer Segmentation Using Unsupervised Learning
3. Energy Consumption Time Series Forecasting
4. Loan Default Risk with Business Cost Optimization
5. Interactive Business Dashboard in Streamlit

---

## Task 1: Term Deposit Subscription Prediction
**Objective:**  
Predict whether a bank customer will subscribe to a term deposit as a result of a marketing campaign.

**Approach:**  
- Load & explore the Bank Marketing dataset  
- Encode categorical features  
- Build classification models: Logistic Regression, Random Forest  
- Evaluate models: Confusion Matrix, F1-Score, ROC Curve  
- Explain model predictions using SHAP

**Key Results & Insights:**  
- Random Forest achieved highest F1-score  
- Important features: age, balance, previous contacts  
- Target customers with higher balance and engagement in campaigns

**Notebook:** `Task1_BankMarketing/Task1_BankMarketing.ipynb`

---

## Task 2: Customer Segmentation Using Unsupervised Learning
**Objective:**  
Cluster customers based on spending habits for targeted marketing strategies.

**Approach:**  
- Exploratory Data Analysis (EDA)  
- K-Means Clustering for segmentation  
- PCA & t-SNE for visualizing clusters  
- Proposed marketing strategies for each segment

**Key Results & Insights:**  
- Identified 3 customer segments: low, medium, high spenders  
- High spenders: focus on premium products  
- Medium spenders: target with discounts & offers  
- Low spenders: retain with loyalty programs

**Notebook:** `Task2_CustomerSegmentation/Task2_CustomerSegmentation.ipynb`

---

## Task 3: Energy Consumption Time Series Forecasting
**Objective:**  
Forecast short-term household energy usage using historical data.

**Approach:**  
- Time series parsing and resampling  
- Feature engineering: hour of day, weekday/weekend  
- Compared ARIMA, Prophet, and XGBoost models  
- Visualized actual vs forecasted energy usage

**Key Results & Insights:**  
- Prophet model performed best with lowest RMSE  
- Hour-of-day is the most significant feature for prediction  
- Insights can help optimize energy consumption planning

**Notebook:** `Task3_EnergyForecasting/Task3_EnergyForecasting.ipynb`

---

## Task 4: Loan Default Risk with Business Cost Optimization
**Objective:**  
Predict loan defaults and minimize business cost by optimizing model threshold.

**Approach:**  
- Cleaned & preprocessed Home Credit Default Risk dataset  
- Built classification models: Logistic Regression, CatBoost  
- Defined business costs for false positives and false negatives  
- Adjusted model threshold to minimize total cost

**Key Results & Insights:**  
- CatBoost achieved highest accuracy and cost-efficient predictions  
- Important features: credit amount, income type, previous loans  
- Threshold optimization significantly reduced business risk

**Notebook:** `Task4_LoanDefaultRisk/Task4_LoanDefaultRisk.ipynb`

---

## Task 5: Interactive Business Dashboard in Streamlit
**Objective:**  
Develop an interactive dashboard for sales, profit, and segment-wise performance analysis.

**Approach:**  
- Cleaned & prepared Global Superstore dataset  
- Built Streamlit dashboard with filters (Region, Category, Sub-Category)  
- Displayed KPIs: Total Sales, Profit, Top 5 Customers

**Key Results & Insights:**  
- Interactive dashboard allows easy exploration of sales data  
- Insights help identify top-performing products and regions  
- Useful for business decision-making

**Notebook:** `Task5_BusinessDashboard/Task5_BusinessDashboard.ipynb`

---

## How to View & Run
1. Clone the repository:
```bash
git clone https://github.com/Muhammadamanoffical/ITSOLERA-AI-Data-Science_Internship_Assignment_2.git
