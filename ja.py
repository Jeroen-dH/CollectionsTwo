from pynput import keyboard
from pynput.keyboard import Controller,Key
from pynput.mouse import Button,Controller
import time
a = 1
word = "hallo goeiemerge"
time.sleep(5)
keyboard = Controller()
mouse = Controller()
# for x in range(5000):
#     mouse.click(Button.left)
#     mouse.release(Button.left)
#     time.sleep(0.01)

# while a <= 20:
#     mouse.click(Button.left)
#     mouse.release(Button.left)
#     if mouse.position(0,0):
#         break
#     a=a+1



# keyboard.type("je oma op een dikke driewielleerdpoishfgsgfyisduf")
# for x in range(30):
#     print(a)
#     keyboard.press("a")
#     keyboard.release("a")
#     a = a + 1
keyboard.type(word)