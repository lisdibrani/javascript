import openai

# Set your OpenAI API key here
openai.api_key = 'YOUR_API_KEY'

def ask_chatbot(question):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"What is {question}?",
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

def main():
    print("AI Chatbot: Hello! I'm here to help you with any questions you have. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("AI Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = ask_chatbot(user_input)
            print("AI Chatbot:", response)

if __name__ == "__main__":
    main()
