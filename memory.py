from collections import deque
from config import MEMORY_LIMIT

class ConversationMemory:
    def __init__(self, limit=MEMORY_LIMIT):
        self.messages = deque(maxlen=limit)

    def add(self, user_message, assistant_message):
        self.messages.append({
            "user": user_message,
            "assistant": assistant_message
        })

    def has_history(self):
        return bool(self.messages)

    def last_user_message(self):
        if not self.messages:
            return None
        return self.messages[-1]["user"]

    def get_messages(self):
        return list(self.messages)

    def clear(self):
        self.messages.clear()


class UserProfile:
    def __init__(self):
        self.name = None

    def extract_name(self, message):
        import re
        patterns = [
            r"my name is\\s+([a-zA-Z]+)",
            r"i am\\s+([a-zA-Z]+)"
        ]
        for pattern in patterns:
            match = re.search(pattern, message, re.IGNORECASE)
            if match:
                return match.group(1).capitalize()
        return None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
