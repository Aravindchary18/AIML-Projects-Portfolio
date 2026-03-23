# 🏠 House Price Prediction — Machine Learning Web App

A professional end-to-end Machine Learning project that predicts house prices using a trained regression model and a Streamlit web interface. This project demonstrates data preprocessing, feature selection, model training using scikit-learn, model evaluation using regression metrics, model persistence with joblib, and deployment-ready application development.

---

## 🌐 Live Demo

🔗 https://house-app-by-aravind.streamlit.app

---

## 🔗 GitHub Repository

https://github.com/Aravindchary18/AIML-Projects-Portfolio/tree/main/house-price-prediction

---

## 🔍 Project Objective

The goal of this project is to build a machine learning model that can predict house prices based on key input features such as living area, number of bedrooms, year built, overall quality, number of bathrooms, and garage capacity. The project also focuses on deploying the model as an interactive web application for real-time predictions.

---

## 🧠 Machine Learning Approach

- Data preprocessing and feature selection were performed using pandas and scikit-learn  
- A Linear Regression model was trained on selected numerical features  
- Model performance was evaluated using regression metrics such as RMSE and R² score  
- The trained model was serialized using joblib and integrated into the Streamlit application for inference  

---

## 🎯 Features Used for Prediction

- GrLivArea (Living Area)  
- BedroomAbvGr (Number of Bedrooms)  
- YearBuilt (Year the house was built)  
- OverallQual (Overall quality rating)  
- FullBath (Number of full bathrooms)  
- GarageCars (Garage capacity)  

---

## 📊 Model Performance

- RMSE: ~35605  
- R² Score: ~0.67  

---

## 🏆 Model Selection

- Linear Regression was selected for its simplicity and effectiveness for this regression task  
- The model provides reasonable predictions based on the selected features  
- Performance was evaluated using RMSE and R² score  

---

## 🖥️ Application Features

- Interactive web interface built with Streamlit  
- Real-time house price prediction based on user input  
- User-friendly input controls (number inputs)  
- Instant regression output (predicted price)  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- scikit-learn  
- NumPy  
- pandas  
- joblib  

---

## 📂 Project Structure

House Price Prediction/
├── README.md  
├── house_app.py  
├── house_model.pkl  
├── house_price_prediction.py  
├── requirements.txt  
├── train.csv  

---

## 🚀 How to Run Locally

1. Clone the repository:

git clone https://github.com/Aravindchary18/AIML-Projects-Portfolio.git

2. Navigate to the project folder:

cd AIML-Projects-Portfolio/house-price-prediction

3. Install dependencies:

pip install -r requirements.txt

4. Run the application:

streamlit run house_app.py

---

## 🌐 Deployment

This application is deployed using Streamlit Community Cloud by connecting the GitHub repository and selecting `house_app.py` as the main file.

---

## 👨‍💻 Author

- Name: Aravind Nannabattuni  
- GitHub: https://github.com/Aravindchary18  

---

## 📌 Key Highlights

- End-to-end machine learning pipeline from training to deployment  
- Feature selection and regression modeling  
- Evaluation using RMSE and R² score  
- Real-time prediction web application  
- Clean integration of trained ML model with Streamlit UI  
- Portfolio-ready project demonstrating practical ML skills  

---

## ⚠️ Disclaimer

This project is developed for educational and portfolio purposes only. The predictions are based on historical data and should not be considered as actual market valuations.