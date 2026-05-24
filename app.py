from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from src.preprocess import preprocess_input

from src.predict import predict_default
from src.utils import prediction_label


app = Flask(__name__)


# -------------------------------------------------------
# Risk Classification Function
# -------------------------------------------------------

def get_risk_level(probability):

    if probability < 0.30:

        return "Low", "low"

    elif probability < 0.60:

        return "Medium", "medium"

    else:

        return "High", "high"


# -------------------------------------------------------
# HOME PAGE
# -------------------------------------------------------

@app.route('/')
def index():

    return render_template('index.html')


# -------------------------------------------------------
# PREDICTION PAGE (GET REQUEST)
# -------------------------------------------------------

@app.route('/predict', methods=['GET'])
def predict_page():

    return render_template(
        'predict.html',
        result=None
    )


# -------------------------------------------------------
# PREDICTION ROUTE (POST REQUEST)
# -------------------------------------------------------

@app.route('/predict', methods=['POST'])
def predict():

    try:

        # -------------------------------------------------------
        # Collect User Input
        # -------------------------------------------------------

        input_data = {

            'LIMIT_BAL': float(request.form['limit_bal']),

            'SEX': float(request.form['sex']),

            'EDUCATION': float(request.form['education']),

            'MARRIAGE': float(request.form['marriage']),

            'AGE': float(request.form['age']),

            'PAY_0': float(request.form['pay_0']),

            'PAY_2': float(request.form['pay_2']),

            'PAY_3': float(request.form['pay_3']),

            'PAY_4': float(request.form['pay_4']),

            'PAY_5': float(request.form['pay_5']),

            'PAY_6': float(request.form['pay_6']),

            'BILL_AMT1': float(request.form['bill_amt1']),

            'BILL_AMT2': float(request.form['bill_amt2']),

            'BILL_AMT3': float(request.form['bill_amt3']),

            'BILL_AMT4': float(request.form['bill_amt4']),

            'BILL_AMT5': float(request.form['bill_amt5']),

            'BILL_AMT6': float(request.form['bill_amt6']),

            'PAY_AMT1': float(request.form['pay_amt1']),

            'PAY_AMT2': float(request.form['pay_amt2']),

            'PAY_AMT3': float(request.form['pay_amt3']),

            'PAY_AMT4': float(request.form['pay_amt4']),

            'PAY_AMT5': float(request.form['pay_amt5']),

            'PAY_AMT6': float(request.form['pay_amt6'])
        }


        
        # -------------------------------------------------------
        # Prediction
        # -------------------------------------------------------

        processed_data = preprocess_input(input_data)

        prediction, probability = predict_default(processed_data)

        # prediction probability of class 1

        default_probability = float(
            probability[1]
        )

        confidence = float(
            max(probability)
        )

        # -------------------------------------------------------
        # Labels
        # -------------------------------------------------------

        label = prediction_label(
            prediction
        )

        risk_level, risk_class = get_risk_level(
            default_probability
        )

        # -------------------------------------------------------
        # Final Result Dictionary
        # -------------------------------------------------------

        result = {

            'prediction': int(prediction),

            'label': label,

            'probability': default_probability,

            'confidence': confidence,

            'risk_level': risk_level,

            'risk_class': risk_class
        }

    except Exception as e:

        result = {

            'prediction': -1,

            'label': 'Error: Invalid Input',

            'probability': 0,

            'confidence': 0,

            'risk_level': 'Unknown',

            'risk_class': 'medium',

            'error': str(e)
        }

    return render_template(
        'predict.html',
        result=result
    )


# -------------------------------------------------------
# MAIN
# -------------------------------------------------------

if __name__ == '__main__':

    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )