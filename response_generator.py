import random

class ResponseGenerator:
    def __init__(self):
        self.greetings = [
            "Hello! What would you like to explore today?",
            "Hi! I am ready to help you.",
            "Hey! Ask me anything from my knowledge base."
        ]

    def generate(self, message, result, intent, memory, profile):
        if intent == "greeting":
            name = profile.get_name()
            greeting = random.choice(self.greetings)
            return f"{greeting} {name}." if name else greeting

        if intent == "identity":
            return "I am Nova, a Python-based AI assistant. I search my knowledge base, compare text, and use conversation memory."

        if intent == "thanks":
            return "You're welcome! Feel free to ask another question."

        if intent == "help":
            return "I can answer questions about Python, programming, AI, machine learning, data science, computers, and technology. You can also tell me your name or type 'clear memory'."

        if result["answer"]:
            answer = result["answer"]
            if result["score"] > 0.65:
                return answer
            return answer + "\n\nI matched this with a related topic in my knowledge base."

        if memory.has_history():
            previous = memory.last_user_message()
            return f"I could not find a reliable answer for that yet. Your previous question was about: {previous}. Try asking in a different way."

        return "I don't have a strong match for that question yet. Try using a few clear keywords, or ask about Python, AI, machine learning, or computers."
