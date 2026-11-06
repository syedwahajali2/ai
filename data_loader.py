import json
from config import DATA_PATH

def load_knowledge():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        records = json.load(file)

    valid_records = []
    for record in records:
        if all(key in record for key in ("topic", "question", "answer")):
            valid_records.append(record)
    return valid_records
