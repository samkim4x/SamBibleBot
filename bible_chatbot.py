import json
import os
import openai
import tweepy
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# OpenAI API Key (Set as an environment variable)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Twitter API Credentials
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# Authenticate Twitter API
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
twitter_api = tweepy.API(auth, wait_on_rate_limit=True)

def fetch_bible_verse(verse):
    """Retrieve and interpret a Bible verse using OpenAI."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Provide an exegesis and interpretation of the Bible verse: {verse}.",
            max_tokens=500
        )
        return response["choices"][0]["text"].strip()
    except Exception as e:
        logging.error(f"Error fetching Bible verse: {e}")
        return "Error fetching Bible verse. Please try again later."

def tweet_bible_verse(verse, content):
    """Posts a Bible verse with exegesis to Twitter."""
    try:
        tweet = f"{verse}\n{content}\n#Bible #Christianity"
        twitter_api.update_status(tweet[:280])
        return "Tweet posted successfully!"
    except Exception as e:
        logging.error(f"Error posting tweet: {e}")
        return "Error posting tweet. Please try again later."

# Step 1: Refactored 'chatbot' function
def chatbot(user_input=None):
    """Interactive chatbot for Bible study."""
    if user_input is None:
        raise ValueError("No user input provided.")

    logging.info("Welcome to SamBibleBot! Type 'exit' to quit.")

    try:
        if user_input.lower() == "exit":
            logging.info("Goodbye! Keep studying the Word!")
            return "Goodbye!"

        elif user_input.lower().startswith("verse:"):
            verse = user_input.split(":", 1)[1].strip()
            if not verse:
                return "Please provide a valid Bible verse after 'verse:'."
            content = fetch_bible_verse(verse)
            logging.info(f"SamBibleBot: {content}")
            return content

        elif user_input.lower().startswith("tweet:"):
            parts = user_input.split(":", 2)
            if len(parts) >= 3:
                verse = parts[1].strip()
                content = parts[2].strip()
                result = tweet_bible_verse(verse, content)
                logging.info(f"SamBibleBot: {result}")
                return result
            else:
                return "Invalid format. Use 'tweet: verse : content'."

        else:
            return "Invalid command. Use 'verse:' or 'tweet:'."

    except Exception as e:
        logging.error(f"An error occurred in chatbot: {e}")
        return "An unexpected error occurred. Please try again later."

# Step 2: Updated '__main__' block
if __name__ == "__main__":
    # Replace these test inputs with actual API or dynamic inputs during deployment.
    test_inputs = [
        "verse: John 3:16",
        "tweet: John 3:16 : God's love is amazing.",
        "exit",
        "verse: ",  # Edge case: empty verse
        "tweet: Psalm 23:1",  # Edge case: missing content
        "invalid command",  # Edge case: invalid input
    ]

    for test_input in test_inputs:
        logging.info(f"Input: {test_input}")
        response = chatbot(test_input)
        logging.info(f"Response: {response}")


