# Employee Performance Prediction

**Author:** Abhiyanshu Anand  
**Email:** abhiyanshu1107@gmail.com  
**GitHub:** [@abhi1107](https://github.com/abhi1107)

---

## Abstract
This project presents a machine learning-based system to predict employee productivity using real-world garment worker data. The solution includes data preprocessing, model training, evaluation, and a user-friendly web application for real-time predictions.

---

## Introduction
Employee performance prediction is crucial for effective HR management, talent retention, and resource allocation. By leveraging machine learning, organizations can make data-driven decisions to optimize workforce productivity.

---

## Data Description
- **Dataset:** garments_worker_productivity.csv (from Kaggle)
- **Features:**
  - quarter, department, day, team, targeted_productivity, smv, over_time, incentive, idle_time, idle_men, no_of_style_change, no_of_workers, month
- **Target:** actual_productivity

---

## Data Preprocessing
- Dropped columns with >20% missing values (e.g., 'wip')
- Filled remaining missing values (mode for categorical, mean for numeric)
- Converted 'date' to 'month' and dropped original 'date'
- Label encoded categorical features: quarter, department, day

---

## Model Building
- **Algorithms Used:**
  - Linear Regression
  - Random Forest Regressor
  - XGBoost Regressor
- **Train-Test Split:** 80% train, 20% test

---

## Model Evaluation
| Model              | MAE    | MSE    | R² Score |
|--------------------|--------|--------|----------|
| Linear Regression  | 0.108  | 0.022  | 0.19     |
| Random Forest      | 0.067  | 0.012  | 0.56     |
| XGBoost            | 0.073  | 0.015  | 0.43     |

- **Best Model:** Random Forest (highest R², lowest errors)

---

## Feature Importance
- Visualized feature importances for Random Forest and XGBoost
- Key features: team, targeted_productivity, smv, over_time, no_of_workers, etc.

---

## Web App Integration
- Built a Flask web application for user-friendly predictions
- HTML templates for Home, Predict, Submit, and About pages
- Model loaded and used for real-time predictions via web form

---

## Results
- The system predicts employee productivity with good accuracy
- Users can input data and get instant predictions via the web app

---

## Conclusion
This project demonstrates a complete ML workflow from data preprocessing to deployment. The solution can help organizations make informed HR decisions and optimize productivity.

---

## Contact
- **Name:** Abhiyanshu Anand
- **Email:** abhiyanshu1107@gmail.com
- **GitHub:** [@abhi1107](https://github.com/abhi1107) 