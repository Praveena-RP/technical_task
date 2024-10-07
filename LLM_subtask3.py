import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from transformers import pipeline

# Download necessary NLTK resources
nltk.download('punkt')

# Step 1: Load the Data
file_path = 'D:/technical task/cleaned_data.csv'  # Update with your file path
df = pd.read_csv(file_path)

# Step 2: Word Frequency Analysis
def get_most_common_words(text):
    tokens = word_tokenize(text.lower())
    word_counts = Counter(tokens)
    return word_counts.most_common(5)  # Get top 5 most common words

df['Most_Common_Words'] = df['Processed_Content'].apply(get_most_common_words)

# Step 3: Generate Summaries using Hugging Face Transformers
summarizer = pipeline("summarization")

def generate_summary(text):
    # Ensure the text length is manageable for the model (e.g., truncate if too long)
    max_length = 130  # Adjust based on your needs
    return summarizer(text, max_length=max_length, min_length=30, do_sample=False)[0]['summary_text']

df['Summary'] = df['Processed_Content'].apply(generate_summary)

# Step 4: Sentiment Analysis using Hugging Face Transformers
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_analyzer(text)
    return result[0]  # Return the first result

df['Sentiment'] = df['Processed_Content'].apply(analyze_sentiment)

# Step 5: Save results to a new CSV file
output_file_path = 'D:/technical task/analyzed_data.csv'
df.to_csv(output_file_path, index=False)

print("Word frequency analysis, summarization, and sentiment analysis complete. Results saved to analyzed_data.csv.")