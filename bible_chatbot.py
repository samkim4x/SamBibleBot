import json
import os
import openai

# OpenAI API Key (Set as an environment variable)
openai.api_key = os.getenv("OPENAI_API_KEY")

def fetch_bible_verse(verse):
    """Retrieve and interpret a Bible verse using OpenAI."""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Provide an exegesis and interpretation of the Bible verse: {verse}.",
        max_tokens=500
    )
    return response["choices"][0]["text"].strip()

def chatbot(user_input=None):
    """Interactive chatbot for Bible study."""
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
        print("Invalid command. Use 'verse:'.")
        return "Invalid command."

# Step 2: Updated '__main__' block
if __name__ == "__main__":
    # Replace these test inputs with actual API or dynamic inputs during deployment.
    test_inputs = [
        "verse: John 3:16",
        "exit"
    ]

    for test_input in test_inputs:
        response = chatbot(test_input)
        print(f"Response: {response}")
