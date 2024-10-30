import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment_distribution(df):
    """
    Plot the distribution of sentiments.
    :param df: DataFrame, contains sentiment data
    """
    sns.countplot(x='Sentiment', data=df)
    plt.title('Sentiment Distribution')
    plt.show()

def plot_topics(topics):
    """
    Plot the extracted topics.
    :param topics: list of str, topics extracted from topic_extraction.py
    """
    for topic in topics:
        print(topic)

def plot_bottlenecks(bottlenecks):
    """
    Plot bottlenecks such as repeated messages.
    :param bottlenecks: DataFrame or Series containing bottleneck information
    """
    if bottlenecks.empty:
        print("No bottlenecks detected.")
    else:
        print("Bottlenecks:")
        print(bottlenecks)
