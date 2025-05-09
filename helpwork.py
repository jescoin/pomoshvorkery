import pyautogui
import keyboard

f = open('loger.txt', 'r')
f1 = open('fakeusdt.txt', 'r')
if keyboard.is_pressed('П'):
    for line in f:
        pyautogui.typewrite(line)
        pyautogui.press('enter')
if keyboard.is_pressed('З'):
    for line in f1:
        pyautogui.typewrite(line)
        pyautogui.press('enter')