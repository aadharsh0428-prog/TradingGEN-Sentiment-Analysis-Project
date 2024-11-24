# Sentiment Analysis of News Articles

This project provides sentiment analysis of news articles related to various companies using data from the [NewsAPI](https://newsapi.org/). It uses VADER Sentiment Analysis to categorize articles as Positive, Negative, or Neutral, and visualizes the sentiment distribution as pie charts using Plotly.

The project is built with Flask for the web framework, and the sentiment analysis is done using the VADER SentimentIntensityAnalyzer.

---

## Features

- Fetches news articles related to specific companies using the NewsAPI.
- Preprocesses the article content (cleaning text, removing stop words, and lemmatization).
- Performs sentiment analysis using VADER.
- Visualizes sentiment distribution in an interactive pie chart.
- Allows users to select a company and view sentiment results via a web interface.
- Stores sentiment data in MongoDB for persistence and future analysis.

---

## Requirements

To run this project, you'll need the following dependencies:

- Python 3.x
- `Flask` for the web server
- `requests` for API calls
- `pandas` for data handling
- `plotly` for creating charts
- `nltk` for natural language processing
- `vaderSentiment` for sentiment analysis
- `pymongo` for integrating MongoDB

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

---

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

---

## Running the Application

To start the application, run the following command:

```bash
python app.py
```

This will start the Flask development server, and the application will be accessible at:

```
http://127.0.0.1:5000/
```

---

## Using the Web App

1. Visit the homepage of the web app.
2. Select a company from the dropdown list.
3. The app will fetch news articles for the selected company, analyze the sentiment of each article, and display the sentiment distribution in a pie chart.

---

## MongoDB Integration

This project uses MongoDB to store sentiment analysis results for persistence and future querying.

### Storing Data

The sentiment analysis results for each company are saved in the MongoDB `Trading` database, under the `Sentiment` collection. Each document contains:
- Company Name
- Article Title
- Description
- Content
- Published Date
- Sentiment (Positive, Negative, Neutral)
- Compound Score (VADER's detailed sentiment score)
- F1 Score (for model accuracy)

This allows you to query, analyze, and manage the sentiment data over time.

---

## MongoDB Installation and Using MongoDB Compass

### Installing MongoDB:

1. **Download MongoDB Community Server:**
   - Visit the [MongoDB Download Center](https://www.mongodb.com/try/download/community).
   - Select your operating system and download the installer.

2. **Install MongoDB:**
   - Follow the installation instructions specific to your operating system.
   - For Windows, use the `.msi` installer, ensuring you include MongoDB as a Windows service.
   - On macOS or Linux, use the appropriate package manager (e.g., `brew` for macOS or `apt`/`yum` for Linux).

3. **Verify Installation:**
   - Open a terminal or command prompt.
   - Run `mongod --version` to check if MongoDB is installed correctly.
   - Start the MongoDB server using `mongod` (it runs by default on `localhost:27017`).

4. **Create the Database:**
   - MongoDB automatically creates a database when you insert data into it.

---

### Installing MongoDB Compass:

1. **Download MongoDB Compass:**
   - Visit the [MongoDB Compass Download Page](https://www.mongodb.com/products/compass).
   - Select your operating system and download the installer.

2. **Install MongoDB Compass:**
   - Follow the installation process for your operating system.
   - Launch MongoDB Compass once the installation is complete.

---

### Using MongoDB Compass:

1. **Connect to MongoDB:**
   - Open MongoDB Compass.
   - In the connection dialog, enter the connection string. For a local instance, use:
     ```
     mongodb://localhost:27017
     ```
   - Click **Connect**.

2. **Navigate Databases and Collections:**
   - After connecting, you’ll see a list of databases on the server.
   - Click on a database (e.g., `Trading`).
   - Click on a collection (e.g., `Sentiment`) to view its documents.

3. **Insert Data:**
   - Click on a collection and select **Insert Document** to manually add data.
   - Use JSON format for inserting records.

4. **Query Data:**
   - Use the query bar to filter records. For example, to find all positive sentiments:
     ```json
     { "sentiment": "Positive" }
     ```

5. **Edit and Delete Data:**
   - Modify or delete records directly from the UI by selecting the appropriate options in the document viewer.

6. **Visualize Data:**
   - MongoDB Compass provides basic aggregation and visualization tools. Use the **Aggregation** tab to group, sort, or visualize data for insights.

---

With MongoDB and Compass, managing your sentiment analysis data is simple and efficient. You can use the database for extended analysis and integrate it with other tools for more advanced use cases.

---
