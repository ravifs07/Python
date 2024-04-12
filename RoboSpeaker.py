import pyttsx3

if __name__ == '_main_':
    print("Welcome to RoboSpeaker 1.1 created by Ravi Shah")
    
# Initialize the text-to-speech engine
engine = pyttsx3.init()

while True:
    x = input("Enter what you want me to speak (enter 'q' to quit): ")
    if x.lower() == "q":
        engine.say("Bye My Friend Talk to you later.")
        engine.runAndWait()
        break
    else:
        engine.say(x)
        engine.runAndWait()