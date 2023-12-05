# run3.py

# Import necessary modules
import os
import sys
from module2.api import get_reddit_post
from module1.processing import retrieve_comments, save_comments_to_file
from module3.process3 import process_data, save_processed_data_with_index  # Import the modified function

# Check if this script is being run as the main program
if __name__ == "__main__":
    # Check if the command-line arguments include URLs
    if len(sys.argv) < 2:
        print("Usage: python3 run.py URL")
        sys.exit(1)

    # Get the Reddit post URLs from the command-line arguments
    input_file = sys.argv[1]

       # Define Reddit API credentials


    with open(input_file, 'r') as file:
        post_urls = file.read().splitlines()

    for index, post_url in enumerate(post_urls):  # Use enumerate to get the index
        client_id = '4iuS6Vi6nMblW8NXKFudrQ'
        client_secret = '4kkKBJ4_rkD4Bh6ijoiAqQd1MPoTYQ'
        user_agent = 'Maximus<red>'
        # Get the Reddit post data using the specified URL and API credentials
        post = get_reddit_post(post_url, client_id, client_secret, user_agent)

        # Retrieve comments from the Reddit post
        comments = retrieve_comments(post)

        # Process the retrieved comments
        processed_data = process_data(comments)

        # Define the output directory and file path based on the post URL
        output_dir = os.path.join("Data", "processed")
        output_file = os.path.join(output_dir, f"processed_data_{index+1}.txt")  # Use index+1

        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Save the processed data to a text file with index
        save_processed_data_with_index(processed_data, output_file, index+1)

        # Print a message indicating where the processed data was saved
        print(f"Processed data for {post_url} saved to", output_file)
