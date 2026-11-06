import math
from collections import Counter
from text_processor import tokenize, make_ngrams

def document_frequency(documents):
    frequency = Counter()
    for document in documents:
        frequency.update(set(document))
    return frequency

def calculate_score(query_tokens, record, all_records):
    question_tokens = tokenize(record["question"])
    topic_tokens = tokenize(record["topic"])
    keyword_tokens = tokenize(" ".join(record.get("keywords", [])))
    answer_tokens = tokenize(record["answer"])

    query_set = set(query_tokens)
    question_set = set(question_tokens)
    keyword_set = set(keyword_tokens)
    topic_set = set(topic_tokens)

    if not query_set:
        return 0.0

    question_match = len(query_set & question_set) / len(query_set)
    keyword_match = len(query_set & keyword_set) / len(query_set)
    topic_match = len(query_set & topic_set) / len(query_set)
    answer_match = len(query_set & set(answer_tokens)) / len(query_set)

    query_phrases = make_ngrams(query_tokens)
    record_phrases = make_ngrams(question_tokens + keyword_tokens)
    phrase_bonus = 0.12 if query_phrases & record_phrases else 0.0

    score = (
        question_match * 0.42
        + keyword_match * 0.32
        + topic_match * 0.16
        + answer_match * 0.10
        + phrase_bonus
    )
    return min(score, 1.0)

def rank_documents(query_tokens, records):
    scored = []
    for record in records:
        score = calculate_score(query_tokens, record, records)
        if score > 0:
            scored.append({**record, "score": score})
    return sorted(scored, key=lambda item: item["score"], reverse=True)
