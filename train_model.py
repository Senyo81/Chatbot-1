import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Your training data
training_data = [
    ("hi", "greeting"),
    ("yo", "greeting"),
    ("hey", "greeting"),
    ("what's your name?", "ask_name"),
    ("what's the weather in London?", "ask_weather"),
    ("what's the weather in Nairobi?","ask_weather"),
    ("tell me news", "ask_news"),
    ("what's the exchange rate from USD to EUR?", "ask_exchange"),
    ("what's USD to GBP?", "ask_exchange"),
    # add more examples...
]

X_text = [x[0] for x in training_data]
y = [x[1] for x in training_data]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X_text)

model = LogisticRegression()
model.fit(X, y)

# Save the model
with open("intent_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)


