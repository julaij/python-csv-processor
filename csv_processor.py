import pandas as pd
import re

def extract_emails(text):
    # Regular expression to extract emails
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

def process_csv(input_file, output_file, column_name):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Extract emails from the specified column
    df['Extracted_Emails'] = df[column_name].apply(lambda x: extract_emails(str(x)))

    # Save the results to a new CSV file
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Specify input and output file paths
    input_file = "input.csv"
    output_file = "output.csv"
    
    # Specify the column name where emails are located
    column_name = "Emails"
    
    # Process the CSV file
    process_csv(input_file, output_file, column_name)
