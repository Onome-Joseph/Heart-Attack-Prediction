# Heart Attack Prediction Model
## Overview
This project implements a Heart Attack Prediction Machine Learning Model that estimates the likelihood of a heart attack for a patient based on their health parameters. The model uses the **Random Forest algorithm** and achieves very high accuracy, making it a reliable tool for medical analysis and decision-making.
## Applications
- Healthcare Providers: Aid in early diagnosis and risk assessment for heart disease.
- Hospitals: Prioritize patients based on their likelihood of a heart attack, optimizing emergency care.
- Insurance Companies: Assist in risk profiling for health insurance policies.
- Preventive Health Programs: Identify high-risk individuals for targeted interventions.

# Heart Attack Risk Prediction Flask App
This project is a Flask-based web application that predicts the risk of a heart attack based on user input. The prediction is powered by a machine learning model.

## Features
- Interactive form to input patient details.
- Machine learning-based prediction for heart attack risk.
- Easy-to-use interface with a clean design.
---
## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Onome-Joseph/Heart-Attack-Prediction.git
   ```
2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install required dependencies:**
   ```bash
    python
    !pip install Flask
    !pip install numpy
    !pip install scikit-learn
    !pip install pandas
   ```
---

## Running the Application

1. **Ensure the `classifier.pkl` file is in the root directory.**
   This file contains the trained machine learning model. If it's missing, the app will not work.

2. **Start the Flask server:**
   ```bash
   python Heart_attack_FLASK.py
   ```
3. **Access the web application:**
   Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

4. **Fill in the form and get the prediction!**
---
## Project Structure

```
your-repository-name/
│
├── Heart_attack_FLASK.py        # Flask application script
├── classifier.pkl               # Pre-trained machine learning model
├── requirements.txt             # List of Python dependencies
├── templates/
│   └── front.html               # HTML template for the web app (plain design)
│   └──front2.html               # HTML template for the web app (better design)
└── README.md                    # Project documentation
```
---
### Contributions
Contributions are welcome! Feel free to fork the repository, suggest improvements.
