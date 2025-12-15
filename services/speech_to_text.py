from pathlib import Path
import whisper

#Загружается один раз при старте
model = whisper.load_model("base")

def transcribe(audio_path: Path) -> str:
    result = model.transcribe(str(audio_path), language="ru"
)
    return result["text"].strip()