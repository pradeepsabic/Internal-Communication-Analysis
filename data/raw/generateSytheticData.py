import pandas as pd

# Sample email data
email_data = {
    'Message_ID': [1, 2, 3, 4, 5],
    'Sender': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva'],
    'Recipient': ['Bob', 'Alice', 'Alice', 'Alice', 'Bob'],
    'Subject': [
        'Meeting Tomorrow', 
        'Re: Meeting Tomorrow', 
        'Project Update', 
        'Follow-up', 
        'Report Submission'
    ],
    'Message': [
        "Hey Bob, let's meet at 2 PM to discuss the project.",
        "Sounds good! I’ll be there.",
        "Hi Alice, here is the latest update on the project.",
        "Just following up on our last conversation.",
        "Attached is the report for your review."
    ],
    'Timestamp': [
        '2024-01-10 09:00:00', 
        '2024-01-10 09:05:00', 
        '2024-01-10 09:10:00', 
        '2024-01-10 09:15:00', 
        '2024-01-10 09:20:00'
    ]
}

# Sample report data
report_data = {
    'Report_ID': [1, 2, 3, 4, 5],
    'Title': [
        'Quarterly Sales Report', 
        'Project Alpha Update', 
        'Customer Feedback Report', 
        'Market Research Summary', 
        'Internal Audit Findings'
    ],
    'Author': ['Alice', 'Charlie', 'Eva', 'Bob', 'Dave'],
    'Content': [
        'This report summarizes the sales for Q1 and Q2.', 
        'Project Alpha is on schedule with key milestones met.', 
        'Customer feedback has been positive regarding the new features.', 
        'This report covers the latest trends in the market.', 
        'The internal audit revealed areas for improvement.'
    ],
    'Date': ['2024-01-05', '2024-01-08', '2024-01-09', '2024-01-07', '2024-01-04']
}

# Sample meeting transcript data
meeting_data = {
    'Meeting_ID': [1, 2, 3, 4, 5],
    'Participants': [
        'Alice;Bob;Charlie', 
        'Bob;Dave', 
        'Alice;Eva', 
        'Charlie;Eva;Dave', 
        'Alice;Bob;Charlie;Eva'
    ],
    'Notes': [
        'Discussed project timelines and deliverables.', 
        'Evaluated quarterly performance metrics.', 
        'Brainstormed ideas for the upcoming product launch.', 
        'Reviewed customer feedback and proposed changes.', 
        'Finalized budget for the next quarter.'
    ],
    'Date': ['2024-01-10', '2024-01-09', '2024-01-08', '2024-01-06', '2024-01-05']
}

# Create DataFrames
emails_df = pd.DataFrame(email_data)
reports_df = pd.DataFrame(report_data)
meetings_df = pd.DataFrame(meeting_data)

# Save the DataFrames to CSV files
emails_df.to_csv('data/raw/emails.csv', index=False)
reports_df.to_csv('data/raw/reports.csv', index=False)
meetings_df.to_csv('data/raw/meetings.csv', index=False)

print("Dummy data files created:")
print("- data/raw/emails.csv")
print("- data/raw/reports.csv")
print("- data/raw/meetings.csv")
