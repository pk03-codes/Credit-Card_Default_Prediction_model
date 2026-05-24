import joblib 
from src.config import MODEL_PATH

model=joblib.load(MODEL_PATH)

def predict_default(input_data):
    prediction=model.predict(input_data)[0]
    probability=model.predict_proba(input_data)[0]
    return prediction,probability