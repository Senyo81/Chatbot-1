import pickle
import requests
import re

# === Your API Keys ===
WEATHER_API_KEY = "3c8e6fe3c968891bd4e17a2ca9367ab0"
EXCHANGE_API_KEY = "50919b8b9d549e5a70bfe2fd"
NEWS_API_KEY = "7f02bd09985c4b4aaeb3cfd7bfd11867"

# === Load Trained ML Model & Vectorizer ===
with open("intent_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# === Intent Handlers ===

def get_weather_response(message):
    match = re.search(r'weather in (\w+)', message.lower())
    if not match:
        return "Please specify a city like 'weather in London'."
    city = match.group(1)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    res = requests.get(url).json()
    print("Weather API response:", res)
    if res.get("cod") != 200:
        return f"Sorry, I couldn't find the weather for {city}."
    temp = res["main"]["temp"]
    desc = res["weather"][0]["description"]
    return f"The weather in {city} is {desc} with a temperature of {temp}°C."


def get_exchange_response(message):
    match = re.search(r'exchange rate from (\w+) to (\w+)', message.lower())
    if not match:
        return "Please ask like: 'exchange rate from USD to EUR'."
    from_curr, to_curr = match.group(1).upper(), match.group(2).upper()
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/pair/{from_curr}/{to_curr}"
    res = requests.get(url).json()
    print("Exchange API response:", res)
    if res.get("result") != "success":
        return "Sorry, there was a problem fetching the exchange rate."
    rate = res["conversion_rate"]
    return f"1 {from_curr} = {rate} {to_curr}"


def get_news_response(message):
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    res = requests.get(url).json()
    print("News API response:", res)
    if res.get("status") != "ok":
        return "Sorry, I couldn't fetch the news right now."
    articles = res["articles"][:3]
    headlines = [article["title"] for article in articles]
    return "Here are the latest headlines:\n- " + "\n- ".join(headlines)

# === Intent Mapping ===
def get_response(message):
    X_test = vectorizer.transform([message])
    intent = model.predict(X_test)[0]
    print(f"Predicted intent: {intent}")

    if intent == "ask_weather":
        return get_weather_response(message)
    elif intent == "ask_exchange":
        return get_exchange_response(message)
    elif intent == "ask_news":
        return get_news_response(message)
    elif intent == "greeting":
        return "Hello! I'm Smartbot. Ask me about weather, news, or exchange rates."
    elif intent == "ask_name":
        return "I'm Smartbot, your helpful assistant!"
    else:
        return "Sorry, I didn't understand that. Try asking about weather, news, or exchange rates."

