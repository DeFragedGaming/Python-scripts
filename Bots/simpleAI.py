import nltk
import random
from nltk.chat.util import Chat, reflections

# Define a list of patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you|how are things', ['I am good, thank you!', 'I am doing well!', 'Everything is great!']),
    (r'what is your name', ['My name is Chatbot!', 'I am Chatbot, nice to meet you!']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Take care!'])
]

# Create a Chat object with the patterns and reflections
chatbot = Chat(patterns, reflections)

# Start the chatbot
print("Hello, I am a chatbot. How can I help you today?")
while True:
    user_input = input("> ")
    response = chatbot.respond(user_input)
    print(response)