# INFOGENIE

INFOGENIE is an AI-powered chatbot application that provides intelligent responses to user queries by integrating web search and summarization capabilities. It uses **Flask** for the backend, **HTML, CSS, and JavaScript** for the frontend, and integrates **Hugging Face models** along with SmolAgent tools like DuckDuckGo search and text summarization.

## Features

- AI chatbot interface
- Web search using DuckDuckGo
- Text summarization tool
- Dark mode support
- Interactive UI with Tailwind CSS

## Tech Stack

### **Frontend**
- HTML, CSS, JavaScript
- Tailwind CSS

### **Backend**
- Flask (Python)
- SmolAgent (Hugging Face, DuckDuckGo Search, Summarization)
- LiteLLM (for Gemini API integration)

### **Database**
- No database (API-based interaction)

## Installation and Setup

### **Prerequisites**
- Python 3.9+
- Node.js (for frontend development)
- Git
- A virtual environment (recommended)

### **Setup Backend**
```bash
# Clone the repository
git clone https://github.com/Karthikeyasharma979/InfoGenie.git
cd InfoGenie

# Create and activate a virtual environment
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Flask server
python app.py
```

### **Setup Frontend**
```bash
# Open the frontend folder
cd frontend

# Start a local server (using VSCode Live Server or any other method)
```

## API Endpoints

### **1. Chat with AI**
```http
POST /chat
```
**Request Body:**
```json
{
  "message": "What is AI?"
}
```
**Response:**
```json
{
  "response": "AI stands for Artificial Intelligence..."
}
```

## Deployment

### **Deploy Flask App (Backend)**
- You can deploy the Flask backend using **Heroku, Render, or AWS**.

### **Deploy Frontend**
- You can deploy the frontend using **GitHub Pages, Vercel, or Netlify**.

## Troubleshooting

### **CORS Error Fix**
If you encounter a CORS issue when making API requests from the frontend, make sure **Flask-CORS** is enabled:
```python
from flask_cors import CORS
CORS(app)
```

### **ModuleNotFoundError: No module named 'google'**
For Gemini API integration, install the Google dependencies:
```bash
pip install google-auth google-generativeai
```

## Contributors
- **Koratamaddi Karthikeyasharma** - [GitHub](https://github.com/Karthikeyasharma979) | [LinkedIn](https://linkedin.com/in/koratamaddi-karthikeya-sharma-396504194/)


---
📌 **Feel free to contribute, open issues, or suggest improvements!** 🚀

