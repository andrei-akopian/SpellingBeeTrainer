import pyttsx3
import os
import playsound

def gameRound(word):
    print(f"Word: {word}")
    mp3_file = os.path.join(".", f"mp3/{word}.mp3")
    # Check if MP3 file exists
    if os.path.exists(mp3_file):
        # Play the MP3 file
        playsound.playsound(mp3_file)
    else:
        engine.say(word)
        engine.runAndWait()
    # Wait for user confirmation to proceed
    return input("Press Enter to continue...")

# Read the list of words from a text file
with open('words.txt', 'r') as f:
    words = f.read().splitlines()

# Initialize text-to-speech engine
engine = pyttsx3.init()

gameType=input("Linear [L] or Random [R]:")
if gameType in ["L","l","Linear","linear"]:
    #start at
    start=input("Start at (0 by default):")
    if len(start)==0:
        start=0
    elif len(start)<4:
        start=int(start)
    else:
        start=words.index(start)

    for wordI in range(start,len(words)):
        while gameRound(words[wordI])=="r":
            pass

elif gameType in ["R","r","Random","random"]:
    from random import randint
    for i in range(100):
        randI=randint(0,len(words)-1)
        while gameRound(words[randI])=="r":
            pass