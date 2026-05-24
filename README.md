# CrediSENSE
### Machine Learning Powered Credit Default Risk Prediction System

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-WebApp-black?style=flat-square)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)

---

## Overview

CrediSENSE is an end-to-end Machine Learning web application designed to predict the probability of credit card default based on customer demographic, financial, and repayment behavior.

The project combines:
- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Machine Learning Model Training
- Hyperparameter Tuning
- Flask Backend Development
- Frontend Integration

to simulate a real-world AI-powered fintech solution.

---

## Problem Statement

Credit card defaults are one of the major financial risks faced by banks and financial institutions.

Traditional credit scoring systems often fail to capture complex behavioral patterns of customers, leading to delayed risk detection and financial losses.

The objective of this project is to build a Machine Learning system capable of predicting whether a customer is likely to default on their next payment using historical financial and repayment information.

### Business Objectives
- Identify high-risk customers early
- Reduce financial losses
- Improve credit risk assessment
- Support data-driven lending decisions

---

## Dataset Information

This project uses the **Default of Credit Card Clients Dataset** from the UCI Machine Learning Repository.

### Dataset Source
https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients

### Dataset Details

| Attribute | Value |
|---|---|
| Total Records | 30,000 |
| Features | 23 |
| Target Variable | default payment next month |
| Problem Type | Binary Classification |

---

## Project Workflow

```mermaid
%%{init: {'theme':'dark'}}%%

flowchart TD

    A[UCI Credit Card Dataset] --> B[Exploratory Data Analysis]

    B --> C[Data Preprocessing]

    C --> D[Outlier Analysis]

    D --> E[SMOTE for Class Balancing]

    E --> F[Feature Engineering]

    F --> G[Model Training]

    G --> H[Logistic Regression]

    G --> I[Random Forest]

    G --> J[XGBoost]
    G ---> K[Adaboost]
    G ---> L[Gradient Boost]
    G ---> M[Descision Tree]

    H --> O[Model Evaluation]

    I --> O

    J --> O
    K--> O
    L -->O
    M -->O

    N --> P[Hyperparameter Tuning]

    O --> Q[Best Model Selection]

    P --> R[Flask Web Application]

    Q --> S[Real-Time Credit Risk Prediction]
```

---

## System Architecture

```mermaid
%%{init: {
'theme': 'base',
'themeVariables': {
    'primaryColor': '#1e293b',
    'primaryTextColor': '#ffffff',
    'primaryBorderColor': '#38bdf8',
    'lineColor': '#94a3b8',
    'secondaryColor': '#0f172a',
    'tertiaryColor': '#111827',
    'background': '#020617',
    'mainBkg': '#1e293b',
    'secondBkg': '#111827',
    'tertiaryBkg': '#0f172a',
    'clusterBkg': '#111827',
    'clusterBorder': '#38bdf8',
    'edgeLabelBackground':'#020617',
    'fontFamily':'Inter'
}}%%

flowchart LR

    A["👤 User"] --> B["🌐 Frontend UI<br/>HTML • CSS • Jinja"]

    B --> C["⚙️ Flask Backend<br/>app.py"]

    C --> D["🧹 Input Validation<br/>& Form Handling"]

    D --> E["📊 Preprocessing Layer<br/>preprocess.py"]

    E --> F["🤖 Prediction Engine<br/>predict.py"]

    F --> G["🌲 Random Forest Model<br/>Random_Forest.pkl"]

    G --> H["📈 Prediction Probability"]

    H --> I["🚨 Risk Classification<br/>Low • Medium • High"]

    I --> J["📋 Dynamic Result Rendering"]

    J --> B

    B --> K["✅ Final Prediction<br/>Displayed to User"]


    subgraph FRONTEND_LAYER ["🎨 Frontend Layer"]
        B
        J
    end

    subgraph BACKEND_LAYER ["⚡ Backend Layer"]
        C
        D
        E
        F
        I
    end

    subgraph ML_LAYER ["🧠 Machine Learning Layer"]
        G
        H
    end
```

---

## Machine Learning Models Used

- Logistic Regression
- Decision Tree
- Random Forest
- AdaBoost
- Gradient Boosting
- XGBoost

---

## Model Selection

After evaluation, the **Random Forest Classifier** was selected as the final deployed model.

### Why Random Forest?

The model achieved:
- Strong Recall Performance
- Better Generalization
- Stable Cross Validation Performance
- Reduced Overfitting

Since this is a financial risk prediction problem, recall was prioritized to minimize false negatives and avoid missing high-risk customers.

---

## Tech Stack

### Machine Learning
- Scikit-learn
- XGBoost
- Imbalanced-learn

### Data Analysis
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Backend
- Flask

### Frontend
- HTML
- CSS
- Jinja2

---

## Project Structure

```text
RiskLens-AI/
│
├── app.py
│
├── models/
│   └── Random_Forest.pkl
│
├── src/
│   ├── config.py
│   ├── predict.py
│   ├── preprocess.py
│   └── utils.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── predict.html
│
├── static/
│   └── style.css
│
├── notebooks/
│   ├── eda.ipynb
│   ├── preprocessing.ipynb
│   ├── model_training.ipynb
│   └── evaluation.ipynb
│
└── requirements.txt
```

---

## Installation

```bash
git clone (https://github.com/pk03-codes/Credit-Card_Default_Prediction_model.git)
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

---

## Future Improvements

- Docker Integration
- Explainable AI (SHAP)
- Deep Learning Models
- Interactive Dashboard
- LLM-powered Financial Insights

---

## Author

**Priyam Kumar De**

B.Tech Mathematics and Computing  
Machine Learning & AI Enthusiast
