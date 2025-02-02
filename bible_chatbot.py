1  import openai
2  from flask import Flask, request, jsonify
3  import os
4
5  app = Flask(__name__)
6
7  @app.route('/')
8  def home():
9      return "BibleBot is running!"
10
11 @app.route('/chat', methods=['POST'])
12 def chat():
13     user_input = request.json.get("user_input", "")  # Accept user input from the request
14     if not user_input:
15         return jsonify({"error": "No user input provided."}), 400  # Return error if no input
16
17     # Replace this section with your bot's logic
18     try:
19         response = chat_with_bot(user_input)  # Call the chatbot function to handle input
20     except Exception as e:
21         return jsonify({"error": f"An error occurred: {str(e)}"}), 500  # Handle errors
22
23     return jsonify({"response": response})  # Return the bot's response
24
25 def chat_with_bot(user_input):  # Define the chatbot logic
26     openai.api_key = os.getenv("OPENAI_API_KEY")  # Retrieve the API key from the environment
27     prompt = f"You asked: {user_input}\nBibleBot says:"
28     response = openai.Completion.create(
29         engine="text-davinci-003",  # Use the desired OpenAI engine
30         prompt=prompt,
31         max_tokens=150
32     )
33     return response.choices[0].text.strip()  # Extract the bot's response
34
35 if __name__ == '__main__':
36     port = int(os.environ.get('PORT', 5000))  # Default to port 5000 if not specified
37     app.run(host='0.0.0.0', port=port)

from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def fetch_bible_verse(verse):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Explain the Bible verse: {verse}"}
        ],
        max_tokens=500
    )
    return response['choices'][0]['message']['content'].strip()

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
