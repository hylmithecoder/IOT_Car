from check_env.check import check_environment
from scripts.handler_voice import speak
from scripts.handler_request import listen_voice

def main():
    check_environment()
    speak("Welcome Hylmi, How can I help you.", voice_id=0)
    print("Listening...")
    listen_voice()

if __name__ == "__main__":
    main()