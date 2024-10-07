import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Step 1: Load the Data
file_path = 'D:/technical task/all_data_scraped.csv'  # Update with your file path
df = pd.read_csv(file_path)

# Step 2: Drop Unwanted Columns
df.drop(columns=['Title', 'URL'], inplace=True)

# Step 3: Handle Missing Values
print("Missing values before handling:")
print(df.isnull().sum())

# Drop rows where 'Content' is missing
df.dropna(subset=['Content'], inplace=True)

print("Missing values after handling:")
print(df.isnull().sum())

# Step 4: Text Processing Function
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

# Optional: Remove original Content column if not needed anymore
df.drop(columns=['Content'], inplace=True)

# Save cleaned data to a new CSV file
cleaned_file_path = 'D:/technical task/cleaned_data.csv'
df.to_csv(cleaned_file_path, index=False)

print("Data cleaning and preprocessing complete. Cleaned data saved to cleaned_data.csv.")