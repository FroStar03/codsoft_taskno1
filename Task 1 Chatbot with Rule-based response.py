import webbrowser

def chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi Sir how can ii help you"

    elif "how are you" in user_input:
        return "I'm fine is there somethiing i could help with?"

    elif "bye" in user_input:
        return "Goodbye  Have a great day Sir"

    elif "thank you" in user_input:
        return "You're welcome!"

    elif "open" in user_input and "youtube" in user_input:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube..."

    else:
        return "please try again..."

print("Welcome! You can say hello, how are you ,bye, thank, or open YouTube.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chat ended...")
        break
    response = chatbot(user_input)
    print("Bot:", response)
