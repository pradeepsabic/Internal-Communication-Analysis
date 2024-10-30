import os
import pandas as pd  # Add this import for pandas
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch.nn.functional as F
from safetensors.torch import load_file

def load_model_and_tokenizer(model_dir="models/sentiment_model/"):
    """
    Load the pre-trained DistilBERT model and tokenizer from the local disk.
    """
    # Load tokenizer as usual
    tokenizer = DistilBertTokenizer.from_pretrained(model_dir)

    # Load the model using safetensors format
    model_path = os.path.join(model_dir, "model.safetensors")
    state_dict = load_file(model_path)
    model = DistilBertForSequenceClassification.from_pretrained(model_dir, state_dict=state_dict)
    
    return tokenizer, model

def preprocess_text(text, tokenizer):
    """
    Preprocess the input text by tokenizing it using the loaded tokenizer.
    Ensure the input is a string or a list of strings.
    """
    if isinstance(text, str):
        text = [text]  # Convert single string to a list
    elif isinstance(text, pd.Series):  # If it's a Pandas series, convert to list
        text = text.fillna("").tolist()  # Handle NaN values by converting them to empty strings
    elif isinstance(text, list):
        # Ensure all elements are strings (convert any non-string values to empty strings)
        text = [str(t) if t is not None else "" for t in text]
    else:
        raise ValueError("Input text must be a string, a list of strings, or a pandas Series.")

    # Tokenize the text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    return inputs

def predict_sentiment(text, tokenizer, model):
    """
    Predict the sentiment of the input text using the pre-trained DistilBert model.
    """
    inputs = preprocess_text(text, tokenizer)
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Apply softmax to get probabilities
    probs = F.softmax(outputs.logits, dim=-1)
    
    # Get the sentiment label (assuming binary classification: 0 - negative, 1 - positive)
    sentiment = torch.argmax(probs, dim=-1).tolist()  # Convert tensor to list
    return sentiment, probs

def analyze_sentiment(text):
    """
    Main function to load the model, preprocess text, and get sentiment prediction.
    :param text: A single string or a list of strings (or pandas Series)
    :return: Sentiment label and sentiment score
    """
    tokenizer, model = load_model_and_tokenizer()

    # Ensure 'text' is a list of strings if you're passing a DataFrame column
    sentiment, probs = predict_sentiment(text, tokenizer, model)

    # Sentiment label and score for the batch (assuming binary classification)
    results = []
    for i in range(len(text)):
        sentiment_label = "positive" if sentiment[i] == 1 else "negative"
        sentiment_score = probs[i][sentiment[i]].item()
        results.append((sentiment_label, sentiment_score))
    
    return results
