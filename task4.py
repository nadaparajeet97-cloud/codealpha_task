def chatbot():
    responses = {
        "hello": "Hi!",
        "how are you": "I'm fine, thanks!",
        "what is your name": "I am a Python ChatBot.",
        "bye": "Goodbye!"
    }

    print("🤖 ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in responses:
            print("🤖 ChatBot:", responses[user_input])

            if user_input == "bye":
                break
        else:
            print("🤖 ChatBot: Sorry, I don't understand that.")

chatbot()