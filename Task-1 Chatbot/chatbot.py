def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitivity
    user_input = user_input.lower()

    # Define rules and responses
    greetings = ["hello", "hi", "hey", "greetings"]
    farewells = ["bye", "goodbye", "see you", "farewell"]
    questions = ["how are you", "what's up", "how's it going"]
    default_response = "I'm sorry, I don't understand that."

    # Check user input against predefined rules
    if any(word in user_input for word in greetings):
        return "Hello! How can I help you today?"

    elif any(word in user_input for word in farewells):
        return "Goodbye! Have a great day."

    elif any(word in user_input for word in questions):
        return "I'm just a chatbot, but I'm doing well. How about you?"

    else:
        return default_response
# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
