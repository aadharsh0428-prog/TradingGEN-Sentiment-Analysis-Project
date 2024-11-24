import pandas as pd
from preprocess_text import preprocess_text

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
