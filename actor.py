import speech_recognition as sr
from gtts import gTTS
import pyttsx3


def speech_to_text():
    # A recognizer to recognize audio
    r = sr.Recognizer()

    # Using microphone as the source, we could put audio files too
    with sr.Microphone() as source:
        print('Start talking:')

        # A pause before it looks for sound
        r.pause_threshold = 1

        # In case there is music in background, it will ignore it
        r.adjust_for_ambient_noise(source, duration=1)

        # It will listen to the source
        audio = r.listen(source)

        try:
            # This will convert audio to text using google
            message = r.recognize_google(audio)
            print('Text: {}'.format(message))
        # This will capture the noise program doesn't understand
        except sr.UnknownValueError:
            print('I did not understand what you said')
            message = speech_to_text()

        return message


def text_to_speech(message):
    print('AI said: ' + message)
    # Using google text to speech method, set the text to message and language as english
    tts = gTTS(text=message, lang='en')

    # Save the speech on a mp3
    tts.save('audio.mp3')

    # Require a function to run it
    engine = pyttsx3.init()

    # How to turn the speed for the voice, 200 is normal
    engine.setProperty("rate", 200)

    # Volume
    engine.setProperty("volume", 100)

    # Voices 0 is guy, 1 is girl
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)

    # say method take in a string and say it
    engine.say(message)

    engine.runAndWait()


checking = True


def repeat_speech(command):
    text_to_speech(command)
    if command == "exit":
        global checking
        checking = False


# Make the program keep running
while True:
    repeat_speech(speech_to_text())
    if not checking:
        break
