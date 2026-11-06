from data_loader import load_knowledge
from text_processor import clean_text, tokenize
from similarity import rank_documents
from config import MINIMUM_SCORE

class AIBrain:
    def __init__(self):
        self.knowledge = load_knowledge()

    def detect_intent(self, message):
        text = clean_text(message)
        if text in {"bye", "goodbye", "exit", "quit", "close"}:
            return "exit"
        if text in {"clear memory", "forget conversation", "reset chat"}:
            return "clear"
        if text.startswith("my name is ") or text.startswith("i am "):
            return "remember_name"
        if any(word in text.split() for word in {"hello", "hi", "hey", "salam", "assalam"}):
            return "greeting"
        if "your name" in text or "who are you" in text:
            return "identity"
        if "thank" in text:
            return "thanks"
        if any(word in text for word in ["help me", "what can you do", "your features"]):
            return "help"
        return "general"

    def find_answer(self, message):
        query = clean_text(message)
        query_tokens = tokenize(query)
        ranked = rank_documents(query_tokens, self.knowledge)

        if not ranked:
            return {"answer": None, "score": 0.0, "related": []}

        best = ranked[0]
        related = [item["answer"] for item in ranked[1:3] if item["score"] > 0.05]
        if best["score"] < MINIMUM_SCORE:
            return {"answer": None, "score": best["score"], "related": related}

        return {
            "answer": best["answer"],
            "score": best["score"],
            "topic": best["topic"],
            "related": related
        }
