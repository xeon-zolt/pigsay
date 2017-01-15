from gtts import gTTS #to install gtts  write -- > sudo pip install gtts
import os #required for mpg123 to install mpg123 write --> pacman -S mpg123
pyg = 'py'

def original(phrase):
    original= input(str("enter a Word: "))
    if len(original) > 0 and original.isalpha():
        print(original)
        # speak the original word first
        tts = gTTS(text="the original input is " + original, lang='en-us')
        tts.save("pcvoice.mp3")
        os.system("mpg123 -q pcvoice.mp3")
        # tts over
        word = original.lower()
        first = word[0]
        new_word = word+first+pyg
        new_word = new_word[1:len(new_word)]
        return new_word
        # speak pyglatin
        tts = gTTS(text=" piglatin translation is  " + new_word, lang='en-us')
        tts.save("pcvoice.mp3")
        os.system("mpg123 -q pcvoice.mp3")
        # tts over
    elif len(original) > 0 and not original.isalpha():
        print ("only alpha characters accepted")
        orig()
    else:
        print("empty")
        orig()
