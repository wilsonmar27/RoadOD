from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


def types(character):
    keyboard.press(character)
    keyboard.release(character)
    

f = open('text.txt', 'r')
text = f.readlines()
f.close()


time.sleep(5)

for elem in text:
    for char in elem:
        if char == '\n':
            types(Key.enter)
        if char == " ":
            types(char)
        else:
            types(char)
            time.sleep(0.1)
