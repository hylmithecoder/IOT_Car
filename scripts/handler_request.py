import speech_recognition as sr

def listen_voice():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎤 Silakan bicara atau tekan Enter untuk mengetik...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language="id-ID")
            print(f"🗣 Anda berkata: {text}")
            return text
    except sr.UnknownValueError:
        print("⚠ Tidak dapat mengenali suara.")
    except sr.RequestError:
        print("🚨 Kesalahan pada layanan pengenalan suara.")
    except OSError:
        print("🚫 Mikrofon tidak terdeteksi, beralih ke input manual.")
    
    # Jika mikrofon tidak tersedia, gunakan input teks
    return input("⌨ Silakan ketik perintah: ")

# Contoh pemanggilan fungsi
if __name__ == "__main__":
    user_input = listen_voice()
    print(f"📢 Anda memasukkan: {user_input}")
