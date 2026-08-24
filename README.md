# English Conversation AI

A simple local AI application for practicing English conversations using Python, Ollama and Llama 3.2.

The project was created as a practical study project focused on Python, object-oriented programming, conversation history, error handling and persistent data storage.

## Features

- 💬 English conversation with a local AI
- 🧠 Conversation history
- 💾 Persistent conversation memory using JSON
- 🔄 Conversation reset
- ✅ Input validation
- 📝 Error logging
- 🖥️ Simple terminal interface
- 🚫 No paid API required

## Technologies

- Python
- Ollama
- Llama 3.2 3B
- JSON
- Git / GitHub

## Requirements

Before running the project, install:

- Python 3.13 or later
- Ollama
- Llama 3.2 3B

## Installation

### 1. Clone the repository

git clone https://github.com/jaolvz/english-conversation-ai-ollama.git
cd english-conversation-ai-ollama

### 2. Install Python dependencies

pip install -r requirements.txt

### 3. Download the model

ollama pull llama3.2:3b

### 4. Run the application

python main.py

## Available Commands

| Command | Description |
|---|---|
| /help | Show available commands |
| /reset | Reset the conversation |
| /exit | Exit the application |

## Example

You: Hello, my name is João.

AI: Hello João! Nice to meet you. How are you today?

You: I like programming Python.

AI: That's great! What kind of Python projects do you enjoy building?

## Project Structure

english-conversation-ai-ollama/
│
├── data/
│   └── .gitkeep
│
├── logs/
│   └── .gitkeep
│
├── main.py
├── english_AI.py
├── config.py
├── requirements.txt
├── .gitignore
└── README.md

## How It Works

The application uses Ollama to run the Llama 3.2 3B model locally.

The conversation is maintained in memory while the application is running and is also stored in a JSON file so that the conversation can be restored when the application starts again.

The application also limits the amount of conversation history sent to the model to prevent the context from growing indefinitely.

## Project Goals

This project was developed as a practical exercise to improve my knowledge of:

- Python
- Object-oriented programming
- Working with local AI models
- File handling
- JSON
- Error handling
- Logging
- Git and GitHub
- Software project organization

## Future Improvements

Possible future improvements include:

- Voice input and output
- Improved English corrections
- More advanced conversation memory
- Graphical user interface
- Automated tests
- Additional configuration options

## License

This project is available for educational and personal use.