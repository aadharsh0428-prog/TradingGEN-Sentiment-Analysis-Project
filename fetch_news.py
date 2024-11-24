import requests

def fetch_news(api_key, query, from_date, to_date, page_size=100):
    """
    Fetch news articles from the NewsAPI.
    
    Args:
        api_key (str): The API key for accessing the NewsAPI.
        query (str): The search query (company name in this case).
        from_date (str): The start date for fetching news.
        to_date (str): The end date for fetching news.
        page_size (int): The number of articles to fetch.
        
    Returns:
        list: A list of articles.
    """
    url = (
        f"https://newsapi.org/v2/everything?q={query}&from={from_date}&to={to_date}&language=en&pageSize={page_size}&apiKey={api_key}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
        return []
