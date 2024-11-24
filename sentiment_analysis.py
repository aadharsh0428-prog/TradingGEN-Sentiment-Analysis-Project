from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiments_with_vader(df):
    """
    Analyze sentiment for each text using VADER sentiment analysis.
    
    Args:
        df (DataFrame): DataFrame containing the articles' text.
        
    Returns:
        DataFrame: DataFrame with an additional sentiment column.
    """
    analyzer = SentimentIntensityAnalyzer()
    sentiments = []
    for text in df["text"]:
        if text.strip():
            scores = analyzer.polarity_scores(text)
            if scores["compound"] >= 0.05:
                sentiments.append("Positive")
            elif scores["compound"] <= -0.05:
                sentiments.append("Negative")
            else:
                sentiments.append("Neutral")
        else:
            sentiments.append("Neutral")  # Default to Neutral if text is empty
    df["sentiment"] = sentiments
    return df
