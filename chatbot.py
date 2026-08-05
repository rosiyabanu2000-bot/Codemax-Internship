print("=" * 40)
print("      AI STUDY ASSISTANT")
print("=" * 40)
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Goodbye! Happy Learning 😊")
        break

    elif "ai" in user:
        print("Bot: Artificial Intelligence enables machines to perform tasks that usually require human intelligence.")

    elif "machine learning" in user:
        print("Bot: Machine Learning is a branch of AI that allows computers to learn from data.")

    elif "python" in user:
        print("Bot: Python is a popular programming language used in AI, ML, web development, and automation.")

    elif "chatgpt" in user:
        print("Bot: ChatGPT is an AI assistant that helps with coding, writing, learning, and problem solving.")

    elif "gemini" in user:
        print("Bot: Gemini is Google's AI assistant for research, coding, and productivity.")

    elif "copilot" in user:
        print("Bot: Microsoft Copilot helps users write code, create documents, and improve productivity.")

    elif "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help you today?")

    else:
        print("Bot: Sorry, I don't know that yet. Try asking about AI, Python, Machine Learning, ChatGPT, Gemini, or Copilot.")