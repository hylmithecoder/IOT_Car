from .handler_request import VoiceAssistant

def main_loop():
    assistant = VoiceAssistant()
    while True:
        command = assistant.listen_voice()
        if command:
            assistant.execute_command(command)
        print("\n🔄 Menunggu perintah baru... (CTRL+C untuk keluar)")

if __name__ == "__main__":
    main_loop()
