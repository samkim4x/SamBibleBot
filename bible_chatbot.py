import json
import os
import openai

# OpenAI API Key (Set as an environment variable)
openai_api_key = os.getenv("OPENAI_API_KEY")

# Authenticate OpenAI API
openai.api_key = openai_api_key

def fetch_bible_verse(verse):
    """
    Retrieve and interpret a Bible verse using OpenAI.
    """
   response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Specify gpt-3.5-turbo here
    messages=[{"role": "user", "content": f"Provide an exegesis of the Bible verse: {verse}"}],
    max_tokens=500
)

    )
    return response["choices"][0]["text"].strip()

def chatbot(user_input=None):
    """
    Interactive chatbot for Bible study.
    """
    if user_input is None:
        raise ValueError("No user input provided.")

    print("Welcome to SamBibleBot! Type 'exit' to quit.")

    if user_input.lower() == "exit":
        print("Goodbye! Keep studying the Word!")
        return "Goodbye!"

    elif user_input.lower().startswith("verse:"):
        verse = user_input.split(":", 1)[1].strip()
        content = fetch_bible_verse(verse)
        print(f"SamBibleBot: {content}")
        return content

    else:
        print("Invalid command. Use 'verse:' to specify a Bible verse.")
        return "Invalid command."

# Main execution block
if __name__ == "__main__":
    # Replace these test inputs with actual API or dynamic inputs during deployment.
    test_inputs = [
        "verse: John 3:16",
        "exit"
    ]

    for test_input in test_inputs:
        response = chatbot(test_input)
        print(f"Response: {response}")
