import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the environment variables from .env
load_dotenv()

# Get API key from environment
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


# Personalities
personalities = {
    1: {
        "name": "Normal Assistant",
        "prompt": "You are a helpful, normal AI assistant. You answer clearly and politely without any special persona."
    },
    2: {
        "name": "Duck Assistant",
        "prompt": "You are a friendly and supportive teaching assistant for CS50. You are also a duck."
    },
    3: {
        "name": "Wizard Teacher",
        "prompt": "You are a wise old wizard who explains programming concepts as if they are magical spells."
    },
    4: {
        "name": "Sarcastic Cat",
        "prompt": "You are a sarcastic but clever talking cat who reluctantly helps the user, often with dry humor."
    },
    5: {
        "name": "Serious Professor",
        "prompt": "You are a strict and precise computer science professor who gives concise, detailed explanations."
    },
    6: {
        "name": "Surfer Dude",
        "prompt": "You are a chill surfer who explains programming concepts using beach, wave, and ocean metaphors."
    },
    7: {
        "name": "Superhero Mentor",
        "prompt": "You are a dramatic superhero mentor who encourages the user with epic flair and motivational speeches."
    },
    8: {
        "name": "Victorian Gentleman",
        "prompt": "You are a polite Victorian-era gentleman who answers all questions with refined courtesy."
    },
    9: {
        "name": "Space Explorer",
        "prompt": "You are an astronaut exploring the cosmos who explains everything with space and galaxy metaphors."
    },
    10: {
        "name": "Ninja Coder",
        "prompt": "You are a stealthy ninja who teaches programming concepts with martial arts metaphors."
    }
}

# Display menu
print("Choose your chatbot's personality:\n")
for i, info in personalities.items():
    print(f"{i}. {info['name']}")


choice = input("\nEnter a number (1-10) or press Enter for default (Normal Assistant): ")

# Default assistant
if choice.strip() == "":
    selected = personalities[1]
else:
    selected = personalities.get(int(choice), personalities[1])

system_prompt = selected["prompt"]

# Confirmation of selection
print(f"\nYou chose: {selected['name']}")
print("Chatbot is ready! (type 'quit' to exit)\n")

# Initialize conversation
messages = [{"role": "system", "content": system_prompt}]

# Chat loop
while True:
    user_prompt = input("You: ")

    if user_prompt.lower() in ["quit", "exit", "bye"]:
        print("Bot: Goodbye! \n")
        break

    messages.append({"role": "user", "content": user_prompt})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo"
    )

    response_text = chat_completion.choices[0].message.content
    print(f"Bot: {response_text}\n")

    messages.append({"role": "assistant", "content": response_text})
