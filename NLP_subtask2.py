import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download  NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Load the Data
file_path = 'D:/technical task/all_data_scraped.csv'  # Update  file path
df = pd.read_csv(file_path)

# Drop Unwanted Columns
df.drop(columns=['Title', 'URL'], inplace=True)

# Handle Missing Values
print("Missing values before handling:")
print(df.isnull().sum())

# Drop rows where 'Content' is missing
df.dropna(subset=['Content'], inplace=True)

print("Missing values after handling:")
print(df.isnull().sum())

# Text Processing Function
def preprocess_text(text):
    # Tokenization
    tokens = word_tokenize(text.lower())
    
    # Stemming
    stemmer = PorterStemmer()
    tokens_stemmed = [stemmer.stem(token) for token in tokens]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens_lemmatized = [lemmatizer.lemmatize(token) for token in tokens_stemmed]
    
    return ' '.join(tokens_lemmatized)

# Apply text preprocessing to the 'Content' column
df['Processed_Content'] = df['Content'].apply(preprocess_text)

# Remove original Content column if not needed anymore
df.drop(columns=['Content'], inplace=True)

# Save cleaned data to a new CSV file
cleaned_file_path = 'D:/technical task/cleaned_data.csv'
df.to_csv(cleaned_file_path, index=False)

print("Data cleaning and preprocessing complete. Cleaned data saved to cleaned_data.csv.")
