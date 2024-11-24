import plotly.express as px

def visualize_sentiments(df, company_name):
    """
    Visualize the sentiment distribution as a pie chart.
    
    Args:
        df (DataFrame): DataFrame with sentiment analysis results.
        company_name (str): The name of the company for which the sentiment is analyzed.
        
    Returns:
        str: Path to the saved pie chart image.
    """
    sentiment_counts = df["sentiment"].value_counts()
    sentiment_data = sentiment_counts.reset_index()
    sentiment_data.columns = ["sentiment", "count"]

    fig = px.pie(
        sentiment_data,
        names="sentiment",
        values="count",
        title=f"Sentiment Distribution for {company_name}",
        color_discrete_sequence=["#ff9999", "#66b3ff", "#99ff99"],
    )

    # Chart path
    chart_path = f"static/{company_name}_sentiment_chart.html"
    fig.write_html(chart_path)

    return chart_path
