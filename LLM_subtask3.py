import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from transformers import pipeline

# Download NLTK resources
nltk.download('punkt')

# Load the Data
file_path = 'D:/technical task/cleaned_data.csv'  # Update file path
df = pd.read_csv(file_path)

# Word Frequency Analysis
def get_most_common_words(text):
    tokens = word_tokenize(text.lower())
    word_counts = Counter(tokens)
    return word_counts.most_common(5)  

df['Most_Common_Words'] = df['Processed_Content'].apply(get_most_common_words)

# Generate Summaries using Hugging Face Transformers
summarizer = pipeline("summarization")

def generate_summary(text):
    # Ensure the text length is manageable for the model 
    max_length = 130  # Adjust based on  needs
    return summarizer(text, max_length=max_length, min_length=30, do_sample=False)[0]['summary_text']

df['Summary'] = df['Processed_Content'].apply(generate_summary)

# Sentiment Analysis using Hugging Face Transformers
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_analyzer(text)
    return result[0]  # Return the first result

df['Sentiment'] = df['Processed_Content'].apply(analyze_sentiment)

# Save results to a new CSV file
output_file_path = 'D:/technical task/analyzed_data.csv'
df.to_csv(output_file_path, index=False)

print("Word frequency analysis, summarization, and sentiment analysis complete. Results saved to analyzed_data.csv.")
