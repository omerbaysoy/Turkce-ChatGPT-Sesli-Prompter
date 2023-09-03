import os
import time
import pyaudio
import speech_recognition as sr
import playsound
from gtts import gTTS
import openai
import uuid

api_key = "Buraya API anahtarını gir"
lang = 'tr'

openai.api_key = api_key

guy = ""

while True:
    def get_adio():
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
                global guy
                guy = said

                if "Buraya yapay zekanın adını gir" in said:
                    new_string = said.replace("Buraya yapay zekanın adını gir", "")
                    new_string = new_string.strip()
                    print(new_string)
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": new_string}])
                    text = completion.choices[0].message.content
                    speech = gTTS(text=text, lang=lang, slow=False, tld="com.tr")
                    file_name = f"welcome_{str(uuid.uuid4())}.mp3"
                    speech.save(file_name)
                    playsound.playsound(file_name, block=False)

            except Exception as e:
                print(f"Hata: {str(e)}")

        return said

    if "Dur" in guy:
        break

    get_adio()
