import json
from pathlib import Path
from sentence_transformers import SentenceTransformer, util

MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"
model = SentenceTransformer(MODEL_NAME)

TOPICS_PATH = Path("data/topics.json")

def load_topics():
    with open(TOPICS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def detect_intent(text: str) -> dict:
    topics = load_topics()

    query_embedding = model.encode(text, convert_to_tensor=True)

    best_intent = "unknown"
    best_score = 0.0

    for intent, data in topics.items():
        examples = data.get("examples", [])
        description = data.get("description", "")

        corpus = examples + [description]
        topic_embedding = model.encode(corpus, convert_to_tensor=True)

        score = util.cos_sim(query_embedding, topic_embedding).max().item()

        if score > best_score:
            best_score = score
            best_intent = intent

    return {
        "intent": best_intent,
        "confidence": round(best_score, 2)
    }