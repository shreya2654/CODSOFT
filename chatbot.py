while True:
    user_input = input("You: ").lower()

    if "hi" in user_input or "hello" in user_input:
        print("Bot: Hi there! How can I assist you today?")
    elif "how are you" in user_input:
        print("Bot: I'm a chatbot, but I'm here to help you! How are you?")
    elif "help" in user_input:
        print("Bot: Sure, I can help you. Please tell me what you need.")
    elif "what is your name" in user_input:
        print("Bot: I am CodSoftBot, your virtual assistant.")
    elif "thank you" in user_input:
        print("Bot: You're welcome! Happy to help.")
    elif "bye" in user_input or "exit" in user_input:
        print("Bot: Goodbye! Have a great day.")
        break
    else:
        print("Bot: Sorry, I didn’t understand that. Can you please rephrase?")
