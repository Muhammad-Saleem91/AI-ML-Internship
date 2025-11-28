# Task 2: Stock Price Prediction (Time Series)

## 📌 Overview
This task predicts the **Next Day's Closing Price** for Apple (AAPL) stock. I compared **Linear Regression** and **Random Forest Regressor** to analyze how different models handle time-series trends.

## 🧠 Methodology
* **Data Source:** Yahoo Finance (`yfinance` API).
* **Feature Engineering:** Shifted the target variable by -1 day to align "Today's Features" with "Tomorrow's Price".
* **Model Comparison:**
    * **Linear Regression:** Performed best (Lowest MAE) due to its ability to extrapolate linear trends.
    * **Random Forest:** Struggled to predict prices higher than those seen in training (the "Ceiling Effect").

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt