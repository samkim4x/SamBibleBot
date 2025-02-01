1   import json
2   import os
3   import openai
4   import tweepy
5   
6   # OpenAI API Key (Set as an environment variable)
7   openai.api_key = os.getenv("OPENAI_API_KEY")
8   
9   # Twitter API Credentials
10  TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
11  TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
12  TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
13  TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
14  
15  # Authenticate Twitter API
16  auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
17  auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
18  twitter_api = tweepy.API(auth, wait_on_rate_limit=True)
19  
20  def fetch_bible_verse(verse):
21      """Retrieve and interpret a Bible verse using OpenAI."""
22      response = openai.Completion.create(
23          engine="text-davinci-003",
24          prompt=f"Provide an exegesis and interpretation of the Bible verse: {verse}.",
25          max_tokens=500
26      )
27      return response["choices"][0]["text"].strip()
28  
29  def tweet_bible_verse(verse, content):
30      """Posts a Bible verse with exegesis to Twitter."""
31      tweet = f"{verse}\n{content}\n#Bible #Christianity"
32      twitter_api.update_status(tweet[:280])
33      return "Tweet posted successfully!"
34  
35  # Step 1: Refactored `chatbot` function
36  def chatbot(user_input=None):
37      """Interactive chatbot for Bible study."""
38      if user_input is None:
39          raise ValueError("No user input provided.")
40  
41      print("Welcome to SamBibleBot! Type 'exit' to quit.")
42      
43      if user_input.lower() == "exit":
44          print("Goodbye! Keep studying the Word!")
45          return "Goodbye!"
46      elif user_input.lower().startswith("verse:"):
47          verse = user_input.split(":", 1)[1].strip()
48          content = fetch_bible_verse(verse)
49          print(f"SamBibleBot: {content}")
50          return content
51      elif user_input.lower().startswith("tweet:"):
52          parts = user_input.split(":", 2)
53          if len(parts) == 3:
54              verse = parts[1].strip()
55              content = parts[2].strip()
56              result = tweet_bible_verse(verse, content)
57              print(f"SamBibleBot: {result}")
58              return result
59          else:
60              print("Invalid format. Use 'tweet: verse : content'.")
61              return "Invalid format."
62      else:
63          print("Invalid command. Use 'verse:' or 'tweet:'.")
64          return "Invalid command."
65  
66  # Step 2: Updated `__main__` block
67  if __name__ == "__main__":
68      # Replace these test inputs with actual API or dynamic inputs during deployment.
69      test_inputs = [
70          "verse: John 3:16",
71          "tweet: John 3:16 : God's love is amazing.",
72          "exit"
73      ]
74  
75      for test_input in test_inputs:
76          response = chatbot(test_input)
77          print(f"Response: {response}")
