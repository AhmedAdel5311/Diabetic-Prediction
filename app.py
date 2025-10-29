import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load your pipeline (model + transformers)
pipeline = pickle.load(open('model.pkl', 'rb'))

# Replace this with your actual feature names from training
feature_names = ['gender', 'age', 'hypertension', 'heart_disease','smoking_history','bmi','HbA1c_level','blood_glucose_level']  # <-- change this

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Read form inputs in the same order as feature_names
        form_values = request.form.to_dict()
        input_df = pd.DataFrame([form_values], columns=feature_names)
        prediction = pipeline.predict(input_df)[0]
        result = "Diabetic" if prediction == 1 else "Not Diabetic"
        return render_template("home.html", prediction_text=f"The Person is {result}")
    except Exception as e:
        return render_template("home.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
