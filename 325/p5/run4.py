import openai
import os
import time

# Set your OpenAI API key
api_key = ""

# Define a function to analyze the sentiment of a comment
def analyze_sentiments(comments):
    sentiments = []
    for comment in comments:
        try:    
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Analyze the sentiment of the following comment in one word: '{comment}'",
                max_tokens=50,
                api_key=api_key
            )
            sentiment = response.choices[0].text.strip()
            sentiments.append((comment, sentiment))
        except openai.error.RateLimitError:
            print("Exceeded rate limit. Pausing for a minute before continuing.")
            time.sleep(60)  # Wait for 60 seconds (adjust as needed)
    return sentiments

# Define a function to perform sentiment analysis for a given file
def perform_sentiment_analysis(input_file_path, output_file_path):
    # Read comments from the input file
    with open(input_file_path, "r", encoding="utf-8") as file:
        comments = file.read().splitlines()

    # Analyze the sentiment of each comment and save the results to an output file
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for i in range(0, len(comments), 3):
            comment_group = comments[i:i+3]
            results = analyze_sentiments(comment_group)
            for result in results:
                output_file.write(f"Comment: {result[0]}\n")
                output_file.write(f"Sentiment: {result[1]}\n")
                output_file.flush()  # Ensure writing to the file
            time.sleep(.5)  # Wait for a minute between groups of comments

# List of input and output file paths
file_paths = [
    ("Data\processed\\processed_data_1.txt",
     "Data\processed\\sentiment_analysis_1.txt"),
    ("Data\processed\\processed_data_2.txt",
     "Data\processed\\sentiment_analysis_2.txt"),
    ("Data\processed\\processed_data_3.txt",
     "Data\processed\\sentiment_analysis_3.txt"),
    ("Data\processed\\processed_data_4.txt",
     "Data\processed\\sentiment_analysis_4.txt"),
     ("Data\processed\\processed_data_5.txt",
      "Data\processed\\sentiment_analysis_5.txt")
]

# Perform sentiment analysis for each file
for input_path, output_path in file_paths:
    perform_sentiment_analysis(input_path, output_path)
