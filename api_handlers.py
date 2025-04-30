# api_handlers.py

import requests
import logging

logging.basicConfig(filename='chatbot.log', level=logging.INFO)

# === Weather API ===
def get_weather_response(message):
    import re
    match = re.search(r'weather in (\w+)', message.lower())
    if not match:
        return "Please specify a city like 'weather in London'."
    city = match.group(1)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    res = requests.get(url).json()
    print("API response:", res)  # <-- INSERT HERE
    if res.get("cod") != 200:
        return f"Sorry, I couldn't find the weather for {city}."
    temp = res["main"]["temp"]
    desc = res["weather"][0]["description"]
    return f"The weather in {city} is {desc} with a temperature of {temp}°C."

# === Exchange Rate API ===
def get_exchange_response(message):
    import re
    match = re.search(r'exchange rate from (\w+) to (\w+)', message.lower())
    if not match:
        return "Please ask like: 'exchange rate from USD to EUR'."
    from_curr, to_curr = match.group(1).upper(), match.group(2).upper()
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/pair/{from_curr}/{to_curr}"
    res = requests.get(url).json()
    print("API response:", res)  # <-- INSERT HERE
    if res.get("result") != "success":
        return "Sorry, there was a problem fetching the exchange rate."
    rate = res["conversion_rate"]
    return f"1 {from_curr} = {rate} {to_curr}"


# === News API ===
def get_news_response(message):
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    res = requests.get(url).json()
    print("API response:", res)  # <-- INSERT THIS LINE
    if res.get("status") != "ok":
        return "Sorry, I couldn't fetch the news right now."
    
    articles = res["articles"][:3]
    headlines = [article["title"] for article in articles]
    return "Here are the latest headlines:\n- " + "\n- ".join(headlines)

