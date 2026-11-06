from brain import AIBrain
from response_generator import ResponseGenerator
from memory import ConversationMemory, UserProfile
from logger import create_logger

class AIAssistant:
    def __init__(self):
        self.brain = AIBrain()
        self.memory = ConversationMemory()
        self.profile = UserProfile()
        self.generator = ResponseGenerator()
        self.logger = create_logger()

    def reply(self, message):
        message = message.strip()
        if not message:
            return "Please type a message so I can help."

        self.logger.info("User sent a message")
        intent = self.brain.detect_intent(message)

        if intent == "exit":
            return "Goodbye! Have a productive day."

        if intent == "clear":
            self.memory.clear()
            return "Conversation memory has been cleared."

        if intent == "remember_name":
            name = self.profile.extract_name(message)
            if name:
                self.profile.set_name(name)
                return f"Nice to meet you, {name}. I will remember your name during this session."

        result = self.brain.find_answer(message)
        response = self.generator.generate(
            message=message,
            result=result,
            intent=intent,
            memory=self.memory,
            profile=self.profile
        )
        self.memory.add(message, response)
        return response
