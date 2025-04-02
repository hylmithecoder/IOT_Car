# import tkinter as tk
from check_env.check import check_environment
from scripts.handler_voice import VoiceHandler
from scripts.handler_request import VoiceAssistant
from scripts.handler_update import main_loop

def main():
    # tk.Tk().withdraw()  # Sembunyikan jendela utama Tkinter
    # tk.Tk().title("Voice Assistant")
    # tk.Tk().geometry("300x200")  # Ukuran jendela Tkinter
    # tk.Tk().iconbitmap("assets/favicon.ico")  # Ganti dengan ikon Anda
    check_environment()

    # Panggil VoiceHandler dan jalankan opening
    voice = VoiceHandler()
    voice.play_opening()  # Ini akan mengucapkan "Welcome Hylmi, how can I assist you?"
    
    # Jalankan loop utama untuk menangani request suara
    main_loop()

if __name__ == "__main__":
    main()
