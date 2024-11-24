import os
import re
import requests
import pandas as pd
from datetime import datetime, timedelta
from pymongo import MongoClient
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.metrics import f1_score

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")  # Connect to the local MongoDB server
db = client["Trading"]  # Connect to the 'Trading' database
sentiment_collection = db["Sentiment"]  # Use the 'Sentiment' collection

# API Key and other settings
API_KEY = "2e6d03fd8c0346b89be5153a65cca20d"  # Replace with your NewsAPI key
COMPANIES = [
    "Apple", "Tesla", "Google", "Microsoft", "Amazon", "Samsung", "Meta", "Netflix",
    "Intel", "IBM", "Cisco", "Oracle", "Adobe", "HP", "Qualcomm", "AMD", "Uber",
    "Lyft", "Spotify", "Zoom", "Salesforce", "PayPal", "Square", "NVIDIA", "Dell",
    "VMware", "Twitter", "Snapchat", "Pinterest", "Shopify", "eBay", "Dropbox",
    "Slack", "GitHub", "Sony", "LG", "Lenovo", "T-Mobile", "AT&T", "Verizon",
    "TikTok", "ByteDance", "WeChat", "Tencent", "Alibaba", "Baidu", "JD.com",
    "Xiaomi", "Huawei", "Ericsson"
]
TO_DATE = datetime.now().strftime("%Y-%m-%d")
FROM_DATE = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")

def fetch_news(api_key, query, from_date, to_date, page_size=100):
    url = (
        f"https://newsapi.org/v2/everything?q={query}&from={from_date}&to={to_date}&language=en&pageSize={page_size}&apiKey={api_key}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
        return []

def preprocess_text(text):
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)  # Remove URLs
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Keep only letters and spaces
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces
    return text

def analyze_sentiments_with_vader(df):
    analyzer = SentimentIntensityAnalyzer()
    sentiments = []
    compound_scores = []
    for text in df["text"]:
        if text.strip():
            scores = analyzer.polarity_scores(text)
            compound_scores.append(scores["compound"])
            if scores["compound"] >= 0.05:
                sentiments.append("Positive")
            elif scores["compound"] <= -0.05:
                sentiments.append("Negative")
            else:
                sentiments.append("Neutral")
        else:
            sentiments.append("Neutral")  # Default to Neutral if text is empty
            compound_scores.append(0.0)  # Default compound score for empty text
    df["sentiment"] = sentiments
    df["compound_score"] = compound_scores
    return df

def generate_dataset(articles):
    """
    Generate a DataFrame from a list of articles.
    
    Args:
        articles (list): A list of articles fetched from the NewsAPI.
        
    Returns:
        DataFrame: A DataFrame containing the articles' data.
    """
    data = {
        "title": [article.get("title", "") for article in articles],
        "description": [article.get("description", "") for article in articles],
        "content": [article.get("content", "") for article in articles],
        "published_at": [article.get("publishedAt", "") for article in articles],
        "url": [article.get("url", "") for article in articles],  # Add the URL of the articles
    }
    df = pd.DataFrame(data)
    df["text"] = df["title"].fillna("") + " " + df["description"].fillna("")
    df["text"] = df["text"].apply(preprocess_text)
    return df

def save_sentiments_to_mongo(df, company_name):
    # Prepare data to insert into MongoDB
    sentiment_data = []
    for _, row in df.iterrows():
        sentiment_data.append({
            "company_name": company_name,
            "title": row["title"],
            "description": row["description"],
            "content": row["content"],
            "published_at": row["published_at"],
            "sentiment": row["sentiment"],
            "compound_score": row["compound_score"],  # Add compound score
            "created_at": datetime.now()
        })
    
    print(f"Prepared {len(sentiment_data)} records for insertion.")
    
    # Insert sentiment data into MongoDB
    if sentiment_data:
        result = sentiment_collection.insert_many(sentiment_data)
        print(f"Inserted {len(result.inserted_ids)} documents into MongoDB.")
    else:
        print("No data to insert.")

# Main process
if __name__ == "__main__":
    for company in COMPANIES:
        print(f"Fetching news for {company}...")
        articles = fetch_news(API_KEY, company, FROM_DATE, TO_DATE)
        
        if not articles:
            print(f"No articles found for {company}.")
            continue
        
        print(f"Fetched {len(articles)} articles for {company}.")
        
        df = generate_dataset(articles)
        print(f"Generated dataset with {len(df)} rows.")
        
        df = analyze_sentiments_with_vader(df)
        print("Sentiment analysis complete.")
        
        save_sentiments_to_mongo(df, company)
