# 🧠 Stroke Prediction App – Machine Learning for Early Detection

[![Streamlit App](https://img.shields.io/badge/Live_App-Streamlit-success?style=flat&logo=streamlit)](https://tejas28strokeprediction.streamlit.app/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 📌 Project Overview

The **Stroke Prediction App** is a machine learning-powered web application designed to **predict the likelihood of a stroke** in a patient using clinical, lifestyle, and demographic features. The goal is to enable **early intervention and prevention**, thereby reducing stroke-related fatalities.

> Stroke is the **second leading cause of death globally**, as per WHO. Fortunately, timely prediction can save lives — and this app demonstrates how machine learning can power **preventive healthcare**.

## 📖 Inspiration

This project is inspired by the academic study published in *Scientific Reports (Nature Portfolio, 2024)*:  
🔗 [Read the original research](https://www.nature.com/articles/s41598-024-61665-4#ref-CR3ty)

## 💡 Key Features

- **Dataset**: Based on McKinsey EHR records (via Kaggle) – 5,110 real patient records from Bangladesh.
- **Preprocessing**:
  - Missing values (BMI) handled via **median imputation**
  - **Label Encoding** for categorical variables
  - **SMOTE** to balance stroke/non-stroke classes
- **Feature Engineering**:
  - **Statistical selection** using Chi-square, Mutual Information, and VIF
- **Model Development**:
  - Baseline: **Logistic Regression**
  - Advanced: **Random Forest**, **XGBoost**, **Extreme Gradient Boosting**
- **Explainability**:
  - **SHAP** used to interpret model outputs
- **Deployment**:
  - Functional web app built using **Streamlit**
  - UI for real-time prediction with user-provided inputs

## 🚀 Live Demo

👉 Try the live app: [https://tejas28strokeprediction.streamlit.app/](https://tejas28strokeprediction.streamlit.app/)

## 🧠 Model Performance

- **XGBoost** Model on balanced dataset:
  - Precision: **96%**
  - Recall: **96%**
  - F1 Score: **96%**
  - AUC-ROC: **99%**
- **Top Predictive Features**:
  - Age
  - Average Glucose Level
  - BMI
  - Hypertension
  - Heart Disease

## 🛠️ Tech Stack

| Component              | Tools/Libraries                         |
|------------------------|-----------------------------------------|
| Programming Language   | Python                                  |
| Data Manipulation      | NumPy, Pandas                           |
| Modeling               | Scikit-learn, XGBoost, RandomForest     |
| Feature Engineering    | Chi2, Mutual Info, VIF                  |
| Imbalance Handling     | SMOTE                                   |
| Explainability         | SHAP                                    |
| Evaluation Metrics     | Accuracy, Precision, Recall, F1, AUC    |
| UI / Deployment        | Gradio (prototype), Streamlit (final), Docker (planned) |

## 📊 Visual Insights

- Correlation Heatmaps to examine feature relationships
- SHAP plots for model explainability
- ROC Curve for evaluating classifier performance

## 📈 Business & Clinical Impact

- Demonstrates how AI can **augment preventive diagnosis** of stroke
- High potential for integration into **clinical decision support systems**
- Can be scaled for **population-level screening**

## 🧪 How to Use

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/stroke-prediction-app.git
   cd stroke-prediction-app
2. Create a virtual environment and install dependencies:
   pip install -r requirements.txt
3. Run the app locally:
   streamlit run app.py
4. Access the UI at http://localhost:8501
5. 🧾 References

    Research Paper: Scientific Reports, Nature Portfolio, 2024

    Dataset: Kaggle EHR Stroke Dataset (McKinsey Bangladesh EHR)

📃 License

This project is licensed under the MIT License. See the LICENSE file for details.

🙋‍♂️ Contact

For collaborations or questions:

Author: Ecube Analytics
Project Lead: Tejas
📧 Email: [aimldstejas@gmail.com]
🌐 LinkedIN: [https://www.linkedin.com/in/tejasddesaiindia/]

