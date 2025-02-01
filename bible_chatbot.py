import json
import os
import openai
import tweepy

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
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Provide an exegesis and interpretation of the Bible verse: {verse}.",
        max_tokens=500
    )
    return response["choices"][0]["text"].strip()

def tweet_bible_verse(verse, content):
    """Posts a Bible verse with exegesis to Twitter."""
    tweet = f"📖 {verse}\n{content}\n#Bible #Christianity"
    twitter_api.update_status(tweet[:280])
    return "Tweet posted successfully!"

def chatbot():
    """Interactive chatbot for Bible study."""
    print("Welcome to SamBibleBot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye! Keep studying the Word!")
            break
        elif user_input.lower().startswith("verse:"):
            verse = user_input.split(":", 1)[1].strip()
            content = fetch_bible_verse(verse)
            print(f"SamBibleBot: {content}")
        elif user_input.lower().startswith("tweet:"):
            parts = user_input.split(":", 2)
            if len(parts) == 3:
                verse = parts[1].strip()
                content = parts[2].strip()
                print(f"SamBibleBot: {tweet_bible_verse(verse, content)}")
            else:
                print("Invalid format. Use 'tweet: verse : content'.")
        else:
            print("Invalid command. Use 'verse:' or 'tweet:'.")

if __name__ == "__main__":
    chatbot()
