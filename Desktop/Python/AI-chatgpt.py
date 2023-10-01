import random

# Dictionary containing predefined responses
responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a computer program, but I'm doing fine. How can I assist you?",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I don't understand. Can you please rephrase or ask a different question?"
}

# Function to generate response based on user input
def get_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    input_lower = user_input.lower()
    
    # Check if input matches predefined responses
    if input_lower in responses:
        return responses[input_lower]
    else:
        return responses["default"]

# Main function to handle user input and get responses
def main():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = get_response(user_input)
            print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    main()
