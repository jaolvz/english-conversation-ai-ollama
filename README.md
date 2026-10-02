# English Conversation AI

An AI-powered desktop application for practicing English conversations using Python, PySide6 and the Groq API.

The project started as a local AI experiment using Ollama and Llama 3.2 and evolved into a graphical desktop application powered by the Groq API.

The main goal is to practice Python development while exploring AI integration, object-oriented programming, API communication, conversation history and desktop application development.

## Features

* 💬 English conversation with AI
* ✏️ Automatic English corrections
* 📚 Explanations of English mistakes in Brazilian Portuguese
* 🧠 Conversation history
* 💾 Persistent conversation memory using JSON
* 🔄 Conversation reset
* ✅ Input validation
* 📝 Error logging
* 🖥️ Graphical interface built with PySide6
* ⚡ Background AI requests using QThread
* 🔐 API key stored using environment variables
* 📦 Structured AI responses using JSON Schema

## Technologies

* Python 3.13+
* PySide6
* Groq API
* `openai/gpt-oss-20b`
* JSON
* python-dotenv
* Git / GitHub

## Requirements

Before running the project, install:

* Python 3.13 or later
* A Groq API key

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/jaolvz/english-conversation-ai-ollama.git

cd english-conversation-ai-ollama
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your Groq API key.

**Never commit your `.env` file to GitHub.**

### 4. Run the application

```bash
python interface.py
```

## How It Works

The application uses the Groq API to communicate with an AI model.

The user sends an English message through the PySide6 interface. The message is processed by the `EnglishAI` class, which sends the conversation history and system instructions to the Groq API.

The AI returns a structured response containing three fields:

```json
{
    "correction": "...",
    "explanation": "...",
    "reply": "..."
}
```

The application then uses these fields to display the response in the graphical interface.

### Response Structure

**Correction**

The user's English sentence is corrected when necessary.

**Explanation**

The English mistake is explained in Brazilian Portuguese.

**Reply**

The AI continues the conversation naturally in English.

When the user's sentence is already correct, the application can display only the conversational response instead of showing an unnecessary correction and explanation.

## Graphical Interface

The application uses PySide6 to provide a desktop interface containing:

* Conversation display
* Message input
* Send button
* Automatic scrolling
* AI response formatting
* Colored corrections and explanations

The application also uses `QThread` to process API requests in the background, preventing the graphical interface from freezing while the AI is generating a response.

## Conversation Memory

The conversation history is stored in a JSON file.

This allows the application to preserve previous messages and provide contextual responses during future interactions.

The application also limits the amount of history sent to the AI to prevent the conversation context from growing indefinitely.

## Project Structure

```text
english-conversation-ai-ollama/

│
├── logs/
│   └── .gitkeep
│
├── interface.py
├── english_AI.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> `.env` is used locally and should not be committed to the repository.

## Project Evolution

### V1 — Ollama

The first version used Ollama and Llama 3.2 to run the AI locally.

Main focus:

* Python
* Object-oriented programming
* Local AI models
* JSON memory
* Error handling
* Logging
* Terminal application

### V2 — PySide6 + Groq

The second version evolved the project into a graphical desktop application.

Main improvements:

* Replaced Ollama with the Groq API
* Added PySide6 graphical interface
* Added structured AI responses
* Added JSON Schema response validation
* Added background processing with QThread
* Improved English correction and explanation
* Improved user experience

## Project Goals

This project was developed as a practical exercise to improve my knowledge of:

* Python
* Object-oriented programming
* APIs
* AI integration
* PySide6
* JSON
* File handling
* Error handling
* Logging
* Multithreading
* Environment variables
* Git and GitHub
* Software project organization

## Future Improvements

Possible future improvements include:

* 🎙️ Voice input and output
* 🔊 Pronunciation practice
* 📊 Learning progress tracking
* 🧠 Improved conversation memory
* 🧪 Automated tests
* ⚙️ Additional application settings
* 📈 User learning statistics

## License

This project is available for educational and personal use.
