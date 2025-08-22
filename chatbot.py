def simple_chatbot():
    print("Hello! I'm a simple rule-based chatbot. Type 'quit' to exit.")
    
    while True:
        user_input = input("\nYou: ").lower()
        
        if user_input == 'quit':
            print("Chatbot: Goodbye! Have a great day!")
            break
            
        elif 'hello' in user_input or 'hi' in user_input or 'hey' in user_input:
            print("Chatbot: Hello there! How can I help you today?")
            
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a computer program, but I'm functioning well! How about you?")
            
        elif 'your name' in user_input:
            print("Chatbot: I'm SimpleBot, your friendly rule-based chatbot!")
            
        elif 'thank' in user_input:
            print("Chatbot: You're welcome! Is there anything else you'd like to know?")
            
        elif 'weather' in user_input:
            print("Chatbot: I'm a simple bot and can't check real-time weather. But I hope it's nice outside!")
            
        elif 'joke' in user_input:
            print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")
            
        elif 'bye' in user_input or 'goodbye' in user_input:
            print("Chatbot: Goodbye! Feel free to come back if you have more questions!")
            break
            
        elif 'help' in user_input:
            print("""Chatbot: I can respond to these types of messages:
            - Greetings (hi, hello, hey)
            - Ask how I am
            - Ask my name
            - Thank me
            - Ask about weather
            - Tell me a joke
            - Say goodbye""")
            
        else:
            print("Chatbot: I'm not sure how to respond to that. Type 'help' to see what I can do!")

if __name__ == "__main__":
    simple_chatbot()
