# ai-chatbot
```markdown
# 🤖 AI Chatbot with Multiple Personalities

## 🚀 Overview  
An interactive AI chatbot built in Python using OpenAI's API. The chatbot supports multiple "personalities," such as a wizard, sarcastic cat, surfer dude, and more. Users can select a personality, then chat in real-time through the terminal.

## ✨ Features  
- 10 different chatbot personalities  
- Real-time conversation loop in the terminal  
- Clean integration with `.env` for API key management  
- Uses OpenAI’s `chat.completions` endpoint  

## 🛠️ Technologies Used  
- Python 3  
- [OpenAI Python SDK](https://github.com/openai/openai-python)  
- dotenv  

## 📂 Installation & Usage  
```bash
# Clone this repository
git clone https://github.com/YOUR_USERNAME/ai-chatbot.git

# Navigate into the folder
cd ai-chatbot

# Install dependencies
pip install -r requirements.txt

# Add your API key to .env
echo "OPENAI_API_KEY=your_api_key_here" > .env

# Run the chatbot
python chatbot.py
