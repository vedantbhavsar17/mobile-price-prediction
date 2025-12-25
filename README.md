# 📱 Mobile Price Prediction using Machine Learning

This project focuses on predicting the price of a mobile phone based on its specifications using machine learning.  
The main goal of this project is to **learn and demonstrate the complete machine learning workflow**, starting from data collection to a trained baseline model.

The project is built step by step with clear separation between data scraping, data cleaning, exploratory data analysis, and model training.

---

## 📌 Project Overview

Mobile phones have many features, including RAM, processor, camera, battery, display, and connectivity options.  
Estimating price manually using all these parameters is difficult.

In this project, machine learning is used to:
- Analyse how different mobile specifications affect price
- Build a baseline regression model
- Create a strong foundation for future optimisation and deployment

---

## 📂 Project Structure

Mobile-Price-Prediction/
├── data/
│   ├── mobiledata.csv
│   └── smartprix.html
├── scraping/
│   └── smartprix_scraper.py
├── notebooks/
│   ├── data_cleaning_eda.ipynb
│   └── model_training.ipynb
├── requirements.txt
└── README.md

---

## 🌐 Data Scraping

The raw data used in this project was collected from the **Smartprix** website using **Selenium**.

### Tools Used
- Selenium WebDriver
- Firefox browser
- GeckoDriver

### Scraping Process
- Opened the Smartprix mobile listings page
- Applied filters directly on the website
- Loaded all mobile products using automated scrolling
- Saved the complete page source as `smartprix.html`

The scraping script is available here:
---

## 📘 Notebook: data_cleaning_eda.ipynb

This notebook focuses on **data cleaning and exploratory data analysis (EDA)**.

### What is done
- Handles missing values (especially ratings)
- Cleans and standardises:
  - Operating system
  - Processor brand
  - Core values
  - Camera megapixels
- Converts boolean features like 5G, NFC, IR Blaster, and fast charging into a numeric format
- Performs EDA to understand:
  - Price distribution
  - RAM vs price relationship
  - Battery vs average price
  - Processor brand vs price
  - Correlation and normality checks

This notebook helps in understanding the data before building any model.

---

## 📘 Notebook: model_training.ipynb

This notebook focuses on **training a baseline machine learning model**.

### What is done
- Uses the cleaned dataset from the previous step
- Applies One-Hot Encoding on:
  - Brand
  - Processor brand
  - Operating system
- Splits data into 80% training and 20% testing
- Trains a Linear Regression model
- Evaluates model performance

---

## 📊 Model Performance (Baseline)

The Linear Regression baseline model achieved the following results:

- **R² Score:** ~0.81  
- **RMSE:** ~14,900  
- **MSE:** ~222,000,000  

### Interpretation
- The model explains around **81% of the variation** in mobile prices
- Predictions differ from actual prices by approximately **₹14–15k**
- This is a strong baseline result without heavy optimisation

---

## 🧠 What I Learned from This Project

- How to scrape real-world data using Selenium
- How to clean messy and inconsistent datasets
- How to perform meaningful EDA
- How to prepare data for machine learning
- How to encode categorical variables
- How to train and evaluate a baseline regression model
- How to structure and document a complete ML project on GitHub

---

## 🚀 Future Improvements

Planned improvements include:
- Feature engineering
- Outlier handling
- Trying advanced models like Random Forest and Gradient Boosting
- Hyperparameter tuning
- Model comparison and optimisation

---

## 🌐 Deployment Plan

After optimising the model, the project will be extended to:
- Deploy the model as a simple web application
- Allow users to input mobile specifications
- Display predicted price and insights

Deployment will be added in future versions of this project.

---

## 🤝 Connect With Me

If you have suggestions, feedback, or improvement ideas, please let me know.

- **LinkedIn:** https://linkedin.com/in/vedant-bhavsar1  
- **GitHub:** https://github.com/vedantbhavsar17  
- **Kaggle:** https://www.kaggle.com/vedantbhavsar43  

---

## ✅ Final Note

This project represents my **learning journey in machine learning**.  
It focuses on clarity, proper workflow, and gradual improvement rather than just final accuracy.

More updates and improvements will be added over time.
