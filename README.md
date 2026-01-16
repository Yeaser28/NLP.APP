# Gemini-NLP-CLI-Application

# 📝 Description

This project is a menu-driven command line NLP application powered by Google Gemini API.
It allows users to sign up, log in, and perform multiple Natural Language Processing tasks such as sentiment analysis, language translation, text summarization, text generation, classification, and more.

The application is built using Python and follows Object-Oriented Programming (OOP) principles for better structure and scalability.

# 🛠️ Features

👤 User Authentication:
Sign up and log in system using username and password.

🧠 Sentiment Analysis:
Analyze text sentiment and classify it as Positive, Negative, or Neutral.

🌍 Language Translation:
Translate text into any target language using AI.

📝 Text Summarization:
Generate concise summaries from long text.

✍️ Text Generation:
Generate AI-based text from user prompts.

🏷️ Text Classification:
Classify input text into predefined categories.

🔎 Text Extraction:
Extract key information from raw text.

🧩 Topic Modeling:
Identify the main topics discussed in the text.

🧠 Named Entity Recognition:
Detect and classify named entities like person, location, organization, etc.

🌐 Language Detection:
Automatically detect the language of the given text.

💻 CLI Based Interface:
Fully interactive terminal-based menu system.

🧱 OOP Based Design:
Clean and modular class-based architecture.

# 💻 Requirements

Python 3.11 or higher

Google Gemini API Key

# 🚀 How to run?

1. Create virtual enviroment:

```bash
   py -3.11 -m venv venv

```
2. Activate enviroment :

```bash
   venv\Scripts\activate
```


3. Install required packages :
```bash
   python -m pip install google-generativeai python-dotenv
```

4. Create a .env file in the project root.

   Add your own Gemini API key like this in .env file:
```bash
   GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
```

5. Run the application:
```bash
   streamlit run app.py  
```

# 🧪 Notes

User data is stored in-memory (dictionary based).

Restarting the program will reset all user accounts.

Suitable for learning, practice, and mini AI projects.

# 🧑‍💻 Author

Yeaser Mustabi Anik

Powered by Google Gemini | Built with Python