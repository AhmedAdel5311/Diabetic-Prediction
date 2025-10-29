🚀 Diabetes Prediction Web App (Flask + Machine Learning + Heroku Deployment)

This project is a web-based Machine Learning application that predicts whether a person has diabetes based on medical inputs. The model is built using Random Forest Classifier and deployed using Flask. The application is Docker-ready and supports deployment on Heroku using Gunicorn.

📌 Features

✅ ML Model saved with pickle

✅ Fully automated preprocessing pipeline

✅ Flask Web Interface for user input

✅ Dockerized for containerized deployment

✅ Ready for Heroku Deployment

✅ Responsive UI with dropdowns and text fields

📊 Dataset Features Used

Feature	Description

gender	Male / Female

age	Age of the individual

hypertension	1 = Yes, 0 = No

heart_disease	1 = Yes, 0 = No

smoking_history	never, former, current, etc.

bmi	Body Mass Index

HbA1c_level	Hemoglobin A1c Level

blood_glucose_level	Blood Glucose Level

🧠 ML Pipeline Overview

The trained machine learning pipeline includes:

OneHotEncoder

MinMaxScaler

RandomForestClassifier

All steps are saved in model.pkl and loaded automatically during prediction.

📂 Project Structure
├── app.py               # Flask Application

├── model.pkl           # Trained ML Model Pipeline

├── requirements.txt     # Python Dependencies

├── Dockerfile          # Docker configuration

├── Procfile            # Heroku startup command

├── templates/
│   └── home.html       # Frontend HTML page

└── README.md           # Documentation

⚙️ Local Setup

🔹 Install Requirements

pip install -r requirements.txt

🔹 Run Application

python app.py


👉 Visit: http://127.0.0.1:5000

☁️ Deploy on Heroku (Without Docker)

✅ Prerequisites

Install Heroku CLI

Login to Heroku:

heroku login

✅ Step-by-Step Deployment

1️⃣ Create a Heroku App

heroku create diabetes-predictor-app


2️⃣ Add Buildpacks (if needed)

heroku buildpacks:add heroku/python


3️⃣ Push Code

git add .

git commit -m "Initial Deploy"

git push heroku main    # or master depending on branch name


4️⃣ Scale Web Dyno

heroku ps:scale web=1


5️⃣ Open the App

heroku open

🐳 Deploy on Heroku using Docker (Container Registry)

✅ Enable Container Deployment

heroku login

heroku container:login

heroku create diabetes-predictor-app

✅ Build & Push Docker Image

heroku container:push web -a diabetes-predictor-app

✅ Release the App

heroku container:release web -a diabetes-predictor-app

✅ Open in Browser

heroku open -a diabetes-predictor-app

📄 Important Files Required for Heroku Deployment
Procfile
web: gunicorn app:app

requirements.txt
Flask

pandas

numpy

scikit-learn

gunicorn

🚀 Future Enhancements

Store input and prediction history in a database

User login and role-based access

Deploy with HTTPS and custom domain