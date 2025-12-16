import re

def extract_city(text: str)->str|None:
    text = text.lower()

    patterns = [
        r"в\s+([а-яё\-]+)",
        r"для\s+([а-яё\-]+)",
        r"погода\s+([а-яё\-]+)"
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return
    match.group(1).capitalize()
    return None