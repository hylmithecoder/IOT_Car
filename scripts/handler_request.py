import speech_recognition as sr
import webbrowser
import os
import urllib.parse
from scripts.handler_voice import VoiceHandler  # Import VoiceHandler

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.voice = VoiceHandler()  # Inisialisasi voice handler

    def listen_voice(self):
        """Memilih mode input: Suara atau Ketikan."""
        print("\n📢 Pilih mode input:")
        print("1️⃣ Suara")
        print("2️⃣ Ketik")
        mode = input("Masukkan pilihan (1/2): ").strip()

        if mode == "1":
            with sr.Microphone() as source:
                print("🎤 Silakan bicara...")
                self.recognizer.adjust_for_ambient_noise(source)
                try:
                    audio = self.recognizer.listen(source)
                    text = self.recognize_text(audio)
                    return text.lower()
                except sr.UnknownValueError:
                    self.voice.speak("Maaf, saya tidak bisa mengenali suara Anda.")
                    return None
                except sr.RequestError:
                    self.voice.speak("Ada masalah dengan layanan pengenalan suara.")
                    return None
        elif mode == "2":
            return input("⌨ Silakan ketik perintah: ").strip().lower()
        else:
            print("❌ Pilihan tidak valid.")
            return None

    def recognize_text(self, audio):
        """Mengubah suara menjadi teks menggunakan Google Speech Recognition."""
        try:
            text = self.recognizer.recognize_google(audio, language="id-ID")
            print(f"🗣 Anda berkata: {text}")
            return text
        except sr.UnknownValueError:
            return None

    def search_youtube(self, query):
        """Mencari video di YouTube berdasarkan input pengguna."""
        search_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
        print(f"🔍 Mencari di YouTube: {query}")
        self.voice.speak(f"Mencari di YouTube: {query}")
        webbrowser.open(search_url)

    def search_spotify(self, query):
        """Mencari lagu di Spotify berdasarkan input pengguna."""
        search_url = f"https://open.spotify.com/search/{urllib.parse.quote(query)}"
        print(f"🎶 Mencari lagu di Spotify: {query}")
        self.voice.speak(f"Memutar lagu {query} di Spotify")
        webbrowser.open(search_url)

    def open_google(self):
        """Membuka Google di browser."""
        print("🌍 Membuka Google...")
        self.voice.speak("Membuka Google")
        webbrowser.open("https://www.google.com")

    def open_maps(self, location):
        """Membuka Google Maps dengan lokasi tertentu."""
        search_url = f"https://www.google.com/maps/search/{urllib.parse.quote(location)}"
        print(f"🗺 Membuka peta lokasi: {location}")
        self.voice.speak(f"Membuka peta lokasi {location}")
        webbrowser.open(search_url)

    def execute_command(self, command):
        """Menjalankan perintah berdasarkan input pengguna."""
        if command:
            if "youtube" in command:
                self.voice.speak("Apa yang ingin Anda cari di YouTube?")
                search_query = input("Masukkan judul video atau channel: ").strip()
                self.search_youtube(search_query)
            
            elif "putar musik" in command or "spotify" in command:
                self.voice.speak("Apa judul lagu yang ingin Anda putar di Spotify?")
                search_query = input("Masukkan judul lagu atau artis: ").strip()
                self.search_spotify(search_query)
            
            elif "buka google" in command:
                self.open_google()
            
            elif "lihat maps" in command or "cari lokasi" in command:
                self.voice.speak("Lokasi apa yang ingin Anda cari?")
                location = input("Masukkan nama lokasi: ").strip()
                self.open_maps(location)
            
            elif "keluar" in command or "stop" in command:
                self.voice.speak("Terima kasih telah menggunakan asisten suara. Sampai jumpa!")
                exit()
            
            else:
                self.voice.speak("Maaf, saya tidak mengenali perintah itu.")

# Jalankan program
if __name__ == "__main__":
    assistant = VoiceAssistant()
    command = assistant.listen_voice()
    assistant.execute_command(command)
