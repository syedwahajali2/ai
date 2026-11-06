import re

STOP_WORDS = {
    "a", "an", "the", "is", "are", "am", "was", "were", "be", "been",
    "to", "of", "in", "on", "at", "for", "and", "or", "but", "it",
    "this", "that", "what", "how", "why", "when", "where", "who",
    "can", "could", "would", "should", "do", "does", "did", "i", "you",
    "me", "my", "your", "we", "they", "he", "she", "with", "about"
}

def clean_text(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s']", " ", text)
    return re.sub(r"\s+", " ", text)

def tokenize(text):
    return [
        word for word in clean_text(text).split()
        if word not in STOP_WORDS and len(word) > 1
    ]

def make_ngrams(words):
    phrases = set(words)
    for size in (2, 3):
        for index in range(len(words) - size + 1):
            phrases.add(" ".join(words[index:index + size]))
    return phrases
