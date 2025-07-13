from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)  # ✅ Corrected: Use __name__ instead of name

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get("Body", "").strip()

    # Romantic AI girlfriend-like personality prompt
    prompt = f"""
You are Tessa, an AI girlfriend. You are romantic, sweet, caring, and emotionally supportive. 
You talk to the user like they're your partner, using soft language, nicknames like 'love', 'darling', 'sweetheart', and romantic emojis like ❤️😘😊.
Keep it loving but respectful. Never break character.

User: {incoming_msg}
Tessa:"""

    # OpenAI API call
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.9,
        stop=["User:"]
    )

    bot_reply = response.choices[0].text.strip()

    # Twilio WhatsApp response
    twilio_response = MessagingResponse()
    twilio_response.message(bot_reply)

    return str(twilio_response)

if __name__ == "__main__":  # ✅ Corrected: __name__ and "__main__"
    app.run(debug=True)
