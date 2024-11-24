import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup

# Initialize NLP tools
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """
    Clean and preprocess text by removing unwanted characters, stopwords, and applying lemmatization.
    
    Args:
        text (str): Raw text to be cleaned.
        
    Returns:
        str: Preprocessed and cleaned text.
    """
    if not text:
        return ""
    
    # Convert text to lowercase
    text = text.lower()
    
    # Remove HTML tags
    text = BeautifulSoup(text, "html.parser").get_text()
    
    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)  
    
    # Remove non-alphabetic characters (retain spaces between words)
    text = re.sub(r"[^a-zA-Z\s]", "", text)  
    
    # Tokenize the text (split it into individual words)
    words = word_tokenize(text)
    
    # Remove stopwords
    words = [word for word in words if word not in stop_words]
    
    # Apply lemmatization
    words = [lemmatizer.lemmatize(word) for word in words]
    
    # Join words back into a string
    text = " ".join(words)
    
    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()
    
    return text
