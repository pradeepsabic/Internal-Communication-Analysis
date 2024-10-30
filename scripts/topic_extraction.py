from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def extract_topics(messages, n_topics=5, n_words=10):
    """
    Extract topics using Latent Dirichlet Allocation (LDA).
    :param messages: list of str, list of messages
    :param n_topics: int, number of topics to extract
    :param n_words: int, number of words per topic
    :return: list of topics with the top words
    """
    print("in topic extraction just before vectorizer")
    print(messages)
    
    # Ensure valid messages
    messages = [msg for msg in messages if isinstance(msg, str) and msg.strip()]
    if not messages:
        print("No valid messages to process!")
        return []
    
    vectorizer = CountVectorizer(max_df=0.99, min_df=1, stop_words='english')
    
    try:
        dtm = vectorizer.fit_transform(messages)
        print("Document-term matrix shape:", dtm.shape)
        
        # Handle cases where n_components might be too large
        n_components = min(n_topics, dtm.shape[1])  # Set n_components to the number of terms if it's smaller than n_topics
        if n_components < 1:
            print("Not enough terms to extract topics.")
            return []
        
        # Apply LDA
        lda = LatentDirichletAllocation(n_components=n_components, random_state=42)
        lda.fit(dtm)
        
        # Extract the top words for each topic
        words = vectorizer.get_feature_names_out()
        topics = []
        
        for topic_idx, topic in enumerate(lda.components_):
            top_words = [words[i] for i in topic.argsort()[-n_words:]]
            topics.append(f"Topic {topic_idx}: {' '.join(top_words)}")
        
        return topics
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
