import os
from twilio.rest import Client
from flask import Flask, request, jsonify
import random
import requests

# Bot creator info
CREATOR = os.getenv("BOT_CREATOR", "Phantomz@jumamohammed")

# Twilio account details (replace these with your own from your Twilio console)
ACCOUNT_SID = 'ACec9c1022b402c04c975822465f06828b'
AUTH_TOKEN = '18c24e39f6ff959178942aa6d81f69bf'
FROM_PHONE = 'whatsapp:+14155238886'  # Replace with your Twilio sandbox number

# Initialize Twilio Client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Create a Flask app to handle incoming webhooks
app = Flask(__name__)

# Helper functions
def get_random_greeting():
    greetings = ["Hi!", "Hello!", "Hey there!", "Greetings!"]
    return random.choice(greetings)

def handle_command(command):
    command = command.lower()  # Normalize to lowercase
    commands = {
        'help': """Here are the available commands:
1. hello - Greet the bot.
2. who made you - Know the creator.
3. !help - List of commands.
4. !joke - Get a random joke.
5. !about - Learn about this bot.""",
        'about': f"This bot is created by {CREATOR} using Twilio's WhatsApp API.",
        'joke': get_joke,
    }

    if command in commands:
        if command == 'joke':
            return commands[command]()  # Calls the get_joke function
        else:
            return commands[command]
    else:
        return "Unknown command. Try '!help' for the list of commands."

def get_joke():
    try:
        response = requests.get('https://official-joke-api.appspot.com/random_joke')
        joke = response.json()
        return f"{joke['setup']} - {joke['punchline']}"
    except requests.exceptions.RequestException:
        return "Sorry, I couldn't fetch a joke right now. Try again later!"

# Flask route to handle incoming messages
@app.route("/incoming", methods=['POST'])
def incoming_message():
    # Get incoming message from the request
    incoming_msg = request.values.get('Body', '').lower()
    from_number = request.values.get('From', '')

    if incoming_msg == 'hello':
        reply_msg = get_random_greeting()
    elif incoming_msg == 'who made you':
        reply_msg = f"I was crafted by {CREATOR}. Let me know if you want to learn more!"
    elif incoming_msg.startswith('!'):
        command = incoming_msg[1:]  # Remove the '!' from the command
        reply_msg = handle_command(command)
    else:
        reply_msg = "I'm not sure what you mean. Try saying 'hello' or 'who made you'."

    # Send the response back to the user
    send_whatsapp_message(from_number, reply_msg)
    return jsonify({'status': 'Message sent'})

def send_whatsapp_message(to, body):
    """Send WhatsApp message via Twilio"""
    message = client.messages.create(
        body=body,
        from_=FROM_PHONE,
        to=to
    )
    print(f"Sent message to {to}: {body}")

# Run the Flask app
if __name__ == "__main__":
    app.run(port=5000)
