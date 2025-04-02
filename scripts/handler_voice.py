import pyttsx3
import random

class VoiceHandler:
    def __init__(self, voice_id=None):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        
        # Pilih suara berdasarkan index, jika tidak, gunakan default
        if voice_id is not None and 0 <= voice_id < len(self.voices):
            self.engine.setProperty('voice', self.voices[voice_id].id)

    def speak(self, text, save_file=False):
        """ Ucapkan teks menggunakan text-to-speech. """
        self.engine.say(text)
        
        if save_file:
            filename = "output.wav"
            self.engine.save_to_file(text, filename)
            print(f"📁 Suara disimpan sebagai {filename}")

        self.engine.runAndWait()

    def play_opening(self):
        """ Ucapkan pesan pembuka saat program dijalankan. """
        opening_messages = [
            "Welcome Hylmi, how can I assist you today?",
            "Hello Hylmi, what do you need?",
            "Hey Hylmi, I'm ready to help!"
        ]
        self.speak(random.choice(opening_messages))

    def respond_to_command(self, command):
        """ Memberikan respons suara berdasarkan perintah yang diberikan. """
        responses = {
            "youtube": [
                "Oke, membuka YouTube sekarang!",
                "Baik, sedang menuju YouTube.",
                "Siap, membuka YouTube untuk Anda."
            ],
            "putar musik": [
                "Tentu, ingin mendengar lagu dari Spotify atau flashdisk?",
                "Baik, saya akan memutar musik untuk Anda.",
                "Musik akan segera diputar, sumbernya dari mana?"
            ],
            "flashdisk": [
                "Mencari musik di flashdisk sekarang.",
                "Sedang mengakses flashdisk, mohon tunggu.",
                "Saya akan mencari lagu yang ada di flashdisk."
            ],
            "spotify": [
                "Membuka Spotify sekarang!",
                "Siap, silakan pilih lagu di Spotify.",
                "Spotify siap digunakan, putar lagu apa?"
            ]
        }

        for key, phrases in responses.items():
            if key in command:
                response_text = random.choice(phrases)
                self.speak(response_text)
                return response_text

        self.speak("Maaf, saya belum mengerti perintah itu.")
        return "Perintah tidak dikenali."

if __name__ == "__main__":
    voice_handler = VoiceHandler()
    while True:
        command = input("\n⌨ Masukkan perintah suara: ").strip().lower()
        if command in ["keluar", "exit", "quit"]:
            print("🚪 Keluar dari program...")
            break
        voice_handler.respond_to_command(command)