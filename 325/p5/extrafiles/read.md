# Project 4: Reddit Comment Scraper and Sentiment Analyzer

This project is designed to scrape and process comments from a specific Reddit post using the PRAW (Python Reddit API Wrapper) library. The project is structured to follow best practices for code organization and modularity.

## Project Structure

The project consists of the following components:

- `modules/` directory: Contains Python modules for different functionalities.
    - `reddit_api.py`: Module for interacting with the Reddit API.
    - `comment_processing.py`: Module for processing comments.
    - `__init__.py`: Empty file to indicate that the directory is a Python package.

- `run3.py`: The Python script that coordinates the execution of the first part of this project. It takes a file of Reddit post URL as a command-line argument and uses the modules to retrieve and process comments.
- `run4.py`: The Python script containing the second part of the project. It takes your previously made processed.txt files and uses devinci from the open ai api to analyze the sentiment of the comments from the Reddit post.

- `Data/` directory: Contains subdirectory and processed data.
    - `processed/`: Stores the processed comment data.
    - `sentiment_analysis.txt`: Stores the sentiments of comments given by the chatbot.
    - `processed_data.txt`: stores the processed comments from the reddit urls.
## Usage

To use this project, follow these steps:

1. Ensure you have Python installed on your system.

2. Clone this GitHub repository to your local machine.

3. Navigate to the project directory:

4. ensure you have the urls you wish to use in `input.txt` (IT MUST BE FORMATTED THE EXACT SAME AS THE EXAMPLE ALREDY IN THE FOLDER)

5. Run the main script `run3.py` with input.txt as a command-line argument. (you may have to use `python 325\p5\\run3.py input.txt` as the command)


6. The script will retrieve comments from the Reddit post and save them to the `Data/processed/` directory as a text file.

7. get a valid Open AI API token and put it in the `run4.py` file on line 6. Info on how to get an API token is in the Dependencies section.

8. run the `run2.py` script on the command line. (you may have to use `python 325\p5\\run4.py` as the command)

9. The script will take your analyzed comments and ask the Devinci chatbot what the sentiment of each comment is, then save it to `sentiment_analysis.txt` 

## Dependencies

This project relies on the following Python libraries:

- `praw`: The Python Reddit API Wrapper. You can install it using pip.
- `openai`: The open ai API accessor. You can install it using pip.

- This project requires that you have a key to the Open AI API, you can follow these steps to get one
  1. Go to `https://openai.com/` and click the login button in the top right

  2. You can create a new account by clicking "create account" next to the continue button or login to a previously made account

  3. After you login to the website, go to the bar on the left side of the screen and click the lock, this will take you to the API keys

  4. click "create new secret key" and give it whatever name you want

  5. copy the key it gives you to somewhere safe but accessible by you.    

- you may use this key in code to make an API request to Open AI. An example of how to make an API request is shown below

      response = openai.Completion.create(
      engine="text-davinci-003",
      #this may be any open ai engine

      prompt="What dinosaurs lived in the cretaceous period?",
      #this is the prompt you are giving the bot, it will respond to what you put here

      max_tokens=60
      #this limits the output length. It is used to limit bandwidth, dont increase too high if you dont need long outputs
        )
