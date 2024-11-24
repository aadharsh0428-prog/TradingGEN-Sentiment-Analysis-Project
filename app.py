from flask import Flask, request, render_template, send_from_directory
from fetch_news import fetch_news
from generate_dataset import generate_dataset
from sentiment_analysis import analyze_sentiments_with_vader
from visualize_sentiments import visualize_sentiments
from datetime import datetime, timedelta

# Flask app initialization
app = Flask(__name__)

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
FROM_DATE = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")  # Last 90 days

@app.route("/", methods=["GET", "POST"])
def home():
    """
    Home route that handles both GET and POST requests for the company sentiment analysis.
    
    Returns:
        Rendered HTML page with sentiment analysis results.
    """
    if request.method == "POST":
        company_name = request.form.get("company")
        if not company_name:
            return render_template(
                "index.html", companies=COMPANIES, error="Please select a company."
            )

        articles = fetch_news(API_KEY, company_name, FROM_DATE, TO_DATE)
        if not articles:
            return render_template(
                "index.html", companies=COMPANIES, error="No articles found for the selected company."
            )

        df = generate_dataset(articles)
        df = analyze_sentiments_with_vader(df)
        chart_path = visualize_sentiments(df, company_name)

        return render_template(
            "index.html",
            companies=COMPANIES,
            chart_path=chart_path,
            selected_company=company_name,
        )

    return render_template("index.html", companies=COMPANIES)

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)  # Disable reloader
