# 🤖 Smartbot — AI-Powered Web Chat Assistant

Smartbot is a machine learning-based chatbot that understands natural language and responds to user queries about:

- 🌦️ Weather
- 💱 Currency Exchange Rates
- 📰 Latest News

It uses an intent classification model (trained on sample data), real-time APIs, and runs via a clean Flask web app interface.

---

## 🌐 Live Demo (Optional GIF/Video/Screenshot)

![Smartbot Screenshot](https://via.placeholder.com/800x400?text=Smartbot+Web+Chat+Demo)

---

## 🧠 Features

- Trained ML model for classifying user intent
- Fetches real data from:
  - OpenWeatherMap API (weather)
  - ExchangeRate-API (currencies)
  - NewsAPI (headlines)
- Runs locally in your browser with Flask
- Simple and clean web UI

---

## 🚀 How to Run Smartbot Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/smartbot.git
cd smartbot


### 2. Set up your virtual environment

python -m venv venv
# Activate it:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate


### 3. Install dependencies

pip install -r requirements.txt


### 4. Add your API keys
Open chatbot_ml.py and replace the placeholders:

WEATHER_API_KEY = "PUT_YOUR_OPENWEATHER_API_KEY_HERE"
EXCHANGE_API_KEY = "PUT_YOUR_EXCHANGERATE_API_KEY_HERE"
NEWS_API_KEY = "PUT_YOUR_NEWSAPI_KEY_HERE"

**You can get free API keys from:**

https://openweathermap.org

https://www.exchangerate-api.com

https://newsapi.org


### 5. Train the ML model

python train_model.py

This creates intent_model.pkl and vectorizer.pkl.


### 6. Run the app

python app.py

Open your browser to: http://localhost:5000



## 💬 Example Questions to Ask Smartbot

“What’s the weather in London?”

“Exchange rate from USD to EUR?”

“Tell me the news”

“Hi there”

“What’s your name?”




##🧪 Tech Stack

Python

Flask

scikit-learn

requests

HTML (Jinja2)

Bootstrap (basic styling)
