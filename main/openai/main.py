#TODO: Add OpenAI api key
import os
import openai
openai.api_key = os.getenv("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")

def audio_to_text(path):
    audio_file = open(path, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

