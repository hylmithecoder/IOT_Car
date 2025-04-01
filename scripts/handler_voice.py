import os
import pyttsx3

def speak(text, voice_id=None):
    """Convert text to speech using pyttsx3."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    if voice_id is not None:
        engine.setProperty('voice', voices[voice_id].id)  # Pilih suara berdasarkan index
    else:
        for idx, voice in enumerate(voices):
            print(f"[{idx}] {voice.name} - {voice.id}")  # Tampilkan semua suara yang tersedia

    engine.say(text)
    engine.save_to_file(text, "output.wav")  # Simpan suara ke file
    engine.runAndWait()

if __name__ == "__main__":
    sample_text = "Selamat datang di sistem suara mobil pintar."
    speak(sample_text)
    print("Text-to-speech conversion complete.")