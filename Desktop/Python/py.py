from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple dictionary for storing responses
responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing fine. How can I assist you?",
    # Add more responses here
}

@app.route('/')
def index():
    return "Chatbot API is running!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message'].lower()  # Convert the message to lowercase for case-insensitive matching
    
    response = responses.get(message, "I'm sorry, I don't understand that.")
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
