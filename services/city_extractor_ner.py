from transformers import pipeline

ner = pipeline(
    "ner",
    model="dslim/bert-base-NER",
    agregation_strategy="simple"
)

def extract_city(text: str)->|None:
    entities=ner(text)

    for entity in entities:
        if entity["entity_group"] in ("LOC", "LOCATION"):
            return entity["word"]

    return None