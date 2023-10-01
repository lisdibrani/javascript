import openai

# Set your OpenAI API key here
openai.api_key = 'YOUR_API_KEY'

def ask_chatbot(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150  # You can adjust the response length as needed
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

def main():
    print("ChatGPT: Hello! I'm here to assist you. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("ChatGPT: Goodbye! Have a great day!")
            break
        else:
            prompt = f"You: {user_input}\nChatGPT:"
            response = ask_chatbot(prompt)
            print(response)

if __name__ == "__main__":
    main()
