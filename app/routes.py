from flask import Blueprint, request, jsonify, render_template
from app.dialogflow_handler import detect_intent_from_text

main = Blueprint('main', __name__)

# Load chatbot page
@main.route('/')
def home():
    return render_template("index.html")

# Chat API
@main.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"response": "No data received"})

        message = data.get("message")

        print("Message received:", message)

        response = detect_intent_from_text(message)

        return jsonify({"response": response})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"response": "Server error occurred"})