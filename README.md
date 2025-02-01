# SamBibleBot
A Bible study AI chatbot that retrieves verses, provides exegesis, integrates with Twitter for theological discussions, and assists in sermon preparation.
## Features
- 📖 **Bible Verse Retrieval**: Retrieve and interpret Bible verses (e.g., `"John 3:16"`).
- 🔍 **Cross-References**: Search topics and related verses (e.g., `"cross-reference: grace"`).
- ✍️ **AI-Powered Writing**: Save, edit, and refine theological writings (e.g., `"edit my writings: grace - God's grace is sufficient."`).
- 🐦 **Twitter Integration**: Auto-tweet Bible verses and insights (e.g., `"tweet verse: Romans 8:28 - All things work together for good..."`).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SamBibleBot.git
   cd SamBibleBot
pip install -r requirements.txt
pip install -r requirements.txt
python bible_chatbot.py
## API Keys Setup
Before running, set up environment variables for:
- OpenAI (`OPENAI_API_KEY`)
- Twitter API (`TWITTER_API_KEY`, `TWITTER_API_SECRET`, `TWITTER_ACCESS_TOKEN`, `TWITTER_ACCESS_SECRET`)

You can set these up in your `.env` file or your hosting platform's environment variable settings.

## How to Use
- **Fetch a Verse**: Type `"John 3:16"` to retrieve and interpret a Bible verse.
- **Search Topics**: Type `"topic: salvation"` to explore a theological topic.
- **Save Writings**: Type `"save my writings: grace - God's grace is sufficient."` to save your content.
- **Edit Writings**: Type `"edit my writings: grace - God's grace is sufficient for all."` to refine and update saved content.
- **Tweet Verses**: Type `"tweet verse: Romans 8:28 - All things work together for good..."` to post Bible verses with insights to Twitter.
