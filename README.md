# Flyfare — AI Flight Price Predictor

Flyfare is a web application built with Django that helps users estimate flight ticket prices using machine learning. I built this to bridge the gap between a complex data science model and a clean, user-friendly interface.

The app takes details like your airline, route, and timing, and gives you a predicted price in both INR and USD.

---

## 🚀 Key Features
- **Real-time Prediction**: Instantly calculates flight costs based on current trends.
- **Dual Currency**: Shows results in Indian Rupees (INR) and US Dollars (USD).
- **Comprehensive Inputs**: Factors in airline, source/destination, number of stops, and how many days are left until departure.
- **Responsive Design**: A modern, clean UI that works well on both desktop and mobile.

---

## 🛠️ Tech Stack
- **Backend**: Django 4.2 (Python)
- **Machine Learning**: Scikit-Learn (Linear Regression), NumPy
- **Storage**: Pickle (for model serialization)
- **Frontend**: HTML5, Vanilla CSS3 (Inter Typography)

---

## 🧠 The Machine Learning Part
The "brain" of this app is a **Linear Regression** model trained on a massive dataset of over **300,000 flight records**. 

- **Accuracy (R² Score)**: ~90.4% (The model is very strong at explaining price variations).
- **Performance**: It uses 8 key features to predict prices with a Mean Absolute Error (MAE) of roughly ₹4,500.
- **Model File**: The trained logic is stored in `flight_model.pkl`.

---

## 💻 How to Run it Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/abhimatdangi/flight_price_prediction.git
   cd flight_price_prediction
   ```

2. **Install Dependencies**
   Make sure you have Python installed, then run:
   ```bash
   pip install django numpy scikit-learn
   ```

3. **Start the Server**
   ```bash
   python manage.py runserver
   ```

4. **Open in Browser**
   Go to `http://127.0.0.1:8000/` and start predicting!

---

## 📂 Project Structure
- `flightproject/`: The core Django configuration and the `.pkl` model.
- `predictor/`: The main logic of the app, including views, templates, and static assets.
- `flight_price_prediction.ipynb`: The original notebook where I cleaned the data and trained the model.

---
