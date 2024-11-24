Sure! Here's the revised `README.md` without the project structure section:

```markdown
# Sentiment Analysis of News Articles

This project provides sentiment analysis of news articles related to various companies using data from the [NewsAPI](https://newsapi.org/). It uses VADER Sentiment Analysis to categorize articles as Positive, Negative, or Neutral, and visualizes the sentiment distribution as pie charts using Plotly.

The project is built with Flask for the web framework, and the sentiment analysis is done using the VADER SentimentIntensityAnalyzer.

## Features

- Fetches news articles related to specific companies using the NewsAPI.
- Preprocesses the article content (cleaning text, removing stop words, and lemmatization).
- Performs sentiment analysis using VADER.
- Visualizes sentiment distribution in an interactive pie chart.
- Allows users to select a company and view sentiment results via a web interface.

## Requirements

To run this project, you'll need the following dependencies:

- Python 3.x
- `Flask` for the web server
- `requests` for API calls
- `pandas` for data handling
- `plotly` for creating charts
- `nltk` for natural language processing
- `vaderSentiment` for sentiment analysis

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

## Setup

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/sentiment-analysis-news.git
cd sentiment-analysis-news
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. **NewsAPI Key**: To use the NewsAPI, you'll need an API key. You can obtain one by signing up on the [NewsAPI website](https://newsapi.org/). 

   - Replace the `API_KEY` in `app.py` with your own key.

## Running the Application

To start the application, run the following command:

```bash
python app.py
```

This will start the Flask development server, and the application will be accessible at:

```
http://127.0.0.1:5000/
```

## Using the Web App

1. Visit the homepage of the web app.
2. Select a company from the dropdown list.
3. The app will fetch news articles for the selected company, analyze the sentiment of each article, and display the sentiment distribution in a pie chart.

## Project Components

- **`app.py`**: The main entry point of the Flask app. Handles requests and integrates all modules.
- **`fetch_news.py`**: Fetches news articles from the NewsAPI based on a given query (company name).
- **`preprocess_text.py`**: Cleans and preprocesses text data by removing URLs, special characters, and stopwords. Tokenizes and lemmatizes words.
- **`sentiment_analysis.py`**: Analyzes the sentiment of text data using the VADER SentimentIntensityAnalyzer.
- **`generate_dataset.py`**: Generates a pandas DataFrame from the fetched articles and preprocesses the text.
- **`visualize_sentiments.py`**: Creates a pie chart showing the distribution of sentiments (Positive, Negative, Neutral).

## Additional Information

- **Sentiment Analysis**: Sentiment is analyzed using the **VADER SentimentIntensityAnalyzer**, which classifies text into Positive, Negative, or Neutral categories based on a compound score.
- **Visualizations**: Sentiment distributions are visualized as interactive pie charts using the Plotly library.

## License

This project is open-source and available under the [MIT License](LICENSE).
```

This version omits the project structure section while keeping the rest of the information intact. You can replace placeholders (like the `git clone` URL) with the actual details for your project.
