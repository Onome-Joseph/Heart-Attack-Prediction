import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
classifier = pickle.load(open('classifier.pkl', 'rb'))

# Define feature names used during training
FEATURE_NAMES = [
    "age", "sex", "cp", "trestbps", "chol", "fbs",
    "restecg", "thalachh", "exang", "oldpeak", "slope", "ca", "thal"
]

@app.route('/')
def home():
    return render_template('front2.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract features from the form
    fig = [float(x) for x in request.form.values()]
    
    # Create a DataFrame with the appropriate feature names
    input_data = pd.DataFrame([fig], columns=FEATURE_NAMES)
    
    # Make the prediction
    prediction = classifier.predict(input_data)
    output = prediction[0]
    
    # Interpret the result
    result = 'No Heart Attack Risk' if output == 0 else 'Heart Attack Risk!'
    
    return render_template('front2.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
