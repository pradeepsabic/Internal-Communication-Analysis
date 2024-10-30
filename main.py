# Import necessary modules
from scripts import preprocess, sentiment_analysis, topic_extraction, bottleneck_detection, team_dynamics, visualization

def run_communication_analysis():
    """
    Main function to run communication analysis for emails, meetings, and reports.
    """
    # Load and preprocess emails data
    print("Loading and preprocessing emails data...")
    emails_data = preprocess.load_data('data/raw/emails.csv')
    emails_data = preprocess.clean_data(emails_data, text_column='Message')

    # Sentiment Analysis on Emails
    print("Running sentiment analysis on emails...")
    sentiment_results = sentiment_analysis.analyze_sentiment(emails_data['Message'])

    # Split the sentiment results into two separate lists for sentiment and score
    sentiments, sentiment_scores = zip(*sentiment_results)

    # Add these as new columns to the DataFrame
    emails_data['Sentiment'] = sentiments
    emails_data['Sentiment_Score'] = sentiment_scores

    # Load and preprocess meetings data
    print("Loading and preprocessing meetings data...")
    meetings_data = preprocess.load_data('data/raw/meetings.csv')
    meetings_data = preprocess.clean_data(meetings_data, text_column='Notes')

    # Sentiment Analysis on Meetings
    print("Running sentiment analysis on meetings...")
    meeting_sentiment_results = sentiment_analysis.analyze_sentiment(meetings_data['Notes'])
    meeting_sentiments, meeting_sentiment_scores = zip(*meeting_sentiment_results)
    meetings_data['Sentiment'] = meeting_sentiments
    meetings_data['Sentiment_Score'] = meeting_sentiment_scores

    # Load and preprocess reports data
    print("Loading and preprocessing reports data...")
    reports_data = preprocess.load_data('data/raw/reports.csv')
    reports_data = preprocess.clean_data(reports_data, text_column='Content')

    # Sentiment Analysis on Reports
    print("Running sentiment analysis on reports...")
    report_sentiment_results = sentiment_analysis.analyze_sentiment(reports_data['Content'])
    report_sentiments, report_sentiment_scores = zip(*report_sentiment_results)
    reports_data['Sentiment'] = report_sentiments
    reports_data['Sentiment_Score'] = report_sentiment_scores

    # Topic Extraction on Emails
    print("Extracting topics from emails...")
    email_topics = topic_extraction.extract_topics(emails_data['Message'])

    # Topic Extraction on Meetings
    print("Extracting topics from meetings...")
    meeting_topics = topic_extraction.extract_topics(meetings_data['Notes'])

    # Topic Extraction on Reports
    print("Extracting topics from reports...")
    report_topics = topic_extraction.extract_topics(reports_data['Content'])

    # Bottleneck Detection on Emails
    print("Detecting bottlenecks in emails data...")
    email_bottlenecks = bottleneck_detection.detect_bottlenecks(emails_data)

    # Bottleneck Detection on Meetings
    print("Detecting bottlenecks in meetings data...")
    meeting_bottlenecks = bottleneck_detection.detect_bottlenecks(meetings_data)

    # Bottleneck Detection on Reports
    print("Detecting bottlenecks in reports data...")
    report_bottlenecks = bottleneck_detection.detect_bottlenecks(reports_data)

    # Team Dynamics Analysis
    print("Analyzing team dynamics from emails, meetings, and reports data...")
    team_dynamics_report = team_dynamics.analyze(emails_data)
    team_dynamics_report_meetings = team_dynamics.analyze(meetings_data)
    team_dynamics_report_reports = team_dynamics.analyze(reports_data)

    # Visualizations
    print("Generating visualizations...")
    visualization.plot_sentiment_distribution(emails_data)
    visualization.plot_sentiment_distribution(meetings_data)
    visualization.plot_sentiment_distribution(reports_data)

    visualization.plot_topics(email_topics)
    visualization.plot_topics(meeting_topics)
    visualization.plot_topics(report_topics)

    visualization.plot_bottlenecks(email_bottlenecks)
    visualization.plot_bottlenecks(meeting_bottlenecks)
    visualization.plot_bottlenecks(report_bottlenecks)

    print("Analysis Complete!")

if __name__ == "__main__":
    run_communication_analysis()
