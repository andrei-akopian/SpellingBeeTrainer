# Spelling Bee Trainer

A commandline app I made for my sister to practice for spelling bee written in Python.

## How it works

The program reads every word word one by one using `pyttsx3` text to speech library. There is also an option to play recorded mp3 files for every word. (It will use the mp3 if there is one, and text to speech if there isn't)

After reading a word the program will wait until the user presses Enter before reading the text one. If the user types in `"r"` and presses Enter, the program will repeat the word.

The program has 2 modes:
- In **Linear** it will interate through every word as it appears in the list. In order to make going around easier, at the beginning the user will be offered to type the word or index of a word to directly skip to that position. (Press Enter to start from the first word by default.)
- In **Random** the program will randomly select a word form the list. 

## Setup

You will need to have a list of words in `words.txt` file. One word on each line (If you are a programmer, append `\n` after each word when parsing/formatting)

You can also add a folder with mp3 files, each file should be called `[word].mp3` (Case sensitive) accordingly.

Now you should have something like this.

```
Spelling Bee Folder
L vocabtrainer.py
L words.txt
    ""
    hello\n
    world\n
    ""
L mp3 (Folder)
    L hello.mp3
    L world.mp3
```

### Running
Navigate to the Spelling Bee Folder from the terminal using `cd` commands. Typing `ls` should give display the 3 items like above.
Type `python3 vocabtrainer.py` into the terminal to run the program.