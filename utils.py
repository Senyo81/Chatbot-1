import re

def extract_city(text):
    match = re.search(r"(?:in|at|from|of)\s+([A-Za-z\s]+)", text)
    if match:
        return match.group(1).strip().title()
    return "London"  # Default

def extract_currencies(text):
    matches = re.findall(r"\b[A-Z]{3}\b", text.upper())
    if len(matches) >= 2:
        return matches[0], matches[1]
    return "USD", "EUR"  # Default

def extract_news_topic(text):
    match = re.search(r"news (?:about|on|regarding)?\s*([A-Za-z\s]+)", text)
    if match:
        return match.group(1).strip().lower()
    return None
