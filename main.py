import os
import speech_recognition as sr
import pyttsx3 as p
import webbrowser as wb
import subprocess
import urllib.parse
import pyautogui
import time
from huggingface_hub import InferenceClient
import config

client = InferenceClient(token=config.HF_TOKEN)

def ask_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="HuggingFaceH4/zephyr-7b-beta",
            messages=[
                {"role": "system", "content": "Reply with the shortest, minimal answers, One or two sentence if possible"},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("AI Error:", repr(e))
        return "AI response failed. Try again later."

brave_path = r"C:\Users\acer\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"
yt_search = "https://www.youtube.com/results?search_query="
engine = p.init()

def say(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("TTS error:", repr(e))

def input_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio, language="en-in")
            return text
        except Exception as e:
            print("Error:", repr(e))
        return None

if __name__ == '__main__':
    run = True
    while run:
        print('Listening')
        text = input_text()
        if text:
            print(text)
            try:
                if "open youtube" in text.lower():
                    say("opening youtube")
                    wb.open("www.youtube.com")

                elif "khud ko band karo" in text.lower():
                    say("bye")
                    run = False

                elif "facebook kholo" in text.lower():
                    command = f'"{brave_path}" --new-window "https://www.facebook.com"'
                    subprocess.Popen(command, shell=True)

                elif "insta kholo" in text.lower():
                    command = f'"{brave_path}" --new-window "https://www.instagram.com/direct/t/17842616496070198/"'
                    subprocess.Popen(command, shell=True)

                elif "open my favourite chat" in text.lower():
                    say("opening your favourite chatbot")
                    wb.open("https://chatgpt.com")

                elif "open gemini" in text.lower():
                    say("Opening gemini AI")
                    wb.open("https://gemini.google.com/")

                elif "close brave" in text.lower():
                    subprocess.run("taskkill /f /im brave.exe", shell=True)
                    say("Brave Browser closed.")

                elif "search in youtube" in text.lower():
                    say("What to search?")
                    search_q = input_text()
                    if search_q:
                        search_url = yt_search + urllib.parse.quote(search_q)
                        wb.open(search_url)
                    else:
                        say("Search input was not understood.")

                elif "shutdown pc karo" in text.lower():
                    say("Are you sure you want to shut down?")
                    confirm = input_text()
                    if "yes" in confirm.lower():
                        for _ in range(15):
                            pyautogui.hotkey('alt', 'f4')
                            time.sleep(0.5)
                        say("Shutting down computer")
                        time.sleep(2)
                        subprocess.run("shutdown /s /f /t 0", shell=True)

                elif "open chat making site" in text.lower():
                    wb.open("https://platform.openai.com/docs/overview")

                elif "close chrome" in text.lower():
                    subprocess.run("taskkill /f /im chrome.exe", shell=True)
                    say("Chrome Browser closed.")

                elif "i want update in you" in text.lower():
                    wb.open("https://www.youtube.com/watch?v=s_8b5iq4Rvk&t=1820s")
                    say("Opening CodewithHarry video")

                elif "check my channel" in text.lower():
                    yt_path = r"C:\Users\acer\Desktop\automation/yt.exe"
                    subprocess.Popen(yt_path, shell=True)

                elif "close this tab" in text.lower():
                    pyautogui.hotkey('ctrl', 'w')
                    say("Tab closed")

                elif "move to first tab" in text.lower():
                    pyautogui.hotkey('ctrl', '1')

                elif "move to second tab" in text.lower():
                    pyautogui.hotkey('ctrl', '2')

                elif "move to third tab" in text.lower():
                    pyautogui.hotkey('ctrl', '3')

                elif "move to fourth tab" in text.lower():
                    pyautogui.hotkey('ctrl', '4')

                elif "move to fifth tab" in text.lower():
                    pyautogui.hotkey('ctrl', '5')

                elif "change window" in text.lower():
                    pyautogui.hotkey("alt", 'tab')

                elif "asking for you" in text.lower():
                    say("AI mode activated.")
                    while True:
                        user_input = input("Prompt : ")
                        if user_input:
                            if "exit ai" in user_input.lower():
                                say("Exiting AI mode.")
                                break
                            print(f"You: {user_input}")
                            response = ask_ai(user_input)
                            print(f"AI: {response}")
                            say(response)

                elif "search in google" in text.lower():
                    query = input_text()
                    if query:
                        search_url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
                        wb.open(search_url)
                    else:
                        say("I didn't understand what to search.")

            except Exception as e:
                print("continue")
        else:
            say("I couldn't catch repeat")
