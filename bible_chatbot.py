from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def home():
    return "BibleBot is running!"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("user_input", "")  # Accept user input from the request
    if not user_input:
        return jsonify({"error": "No user input provided."}), 400  # Return error if no input
    
    try:
        # Generate response using the OpenAI API
        response = fetch_bible_verse(user_input)
        return jsonify({"response": response})  # Return the bot's response
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500  # Handle errors

def fetch_bible_verse(verse):
    """
    Function to fetch explanation for a Bible verse using OpenAI API.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Explain the Bible verse: {verse}"}
        ],
        max_tokens=500
    )
    return response['choices'][0]['message']['content'].strip()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # Default to port 5000 if not specified
    app.run(host='0.0.0.0', port=port)

