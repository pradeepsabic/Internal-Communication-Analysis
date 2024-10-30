import pandas as pd

def detect_bottlenecks(df):
    """
    Detect communication bottlenecks by analyzing response delays and message repetition.
    :param df: DataFrame, contains the communication data
    :return: DataFrame, highlighting bottlenecks
    """
    # Example: Count repeated messages
    repeated_messages = df['Processed_Message'].value_counts()
    bottlenecks = repeated_messages[repeated_messages > 1]
    
    # Identify potential delays based on timestamp if available (assumed 'Timestamp' column exists)
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df['Time_Difference'] = df['Timestamp'].diff()
    
    return bottlenecks
