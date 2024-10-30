import pandas as pd
import re
import spacy

# Load spaCy English model
nlp = spacy.load('en_core_web_sm')

def load_data(file_path):
    """
    Load data from CSV file and return as pandas DataFrame.
    :param file_path: str, path to CSV file
    :return: DataFrame
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

def clean_text_spacy(text):
    """
    Clean and preprocess text using spaCy.
    :param text: str, the text to clean
    :return: str, cleaned text
    """
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Process text with spaCy
    doc = nlp(text.lower())
    
    # Remove stopwords and non-alphabetic tokens, then lemmatize
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    
    # Join tokens back into a single string
    cleaned_text = ' '.join(tokens)
    return cleaned_text

def clean_data(df, text_column):
    """
    Apply cleaning to the entire dataset column using spaCy.
    :param df: DataFrame, the dataset
    :param text_column: str, name of the text column to be cleaned
    :return: DataFrame, with cleaned text column
    """
    df['Processed_Message'] = df[text_column].apply(clean_text_spacy)
    return df

# Example usage:
# df = load_data('your_file.csv')
# cleaned_df = clean_data(df, 'your_text_column')
# print(cleaned_df)
