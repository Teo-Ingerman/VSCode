import pyautogui, keyboard, random, threading

def checkColor(pos):

    x, y = pos

    rgb = pyautogui.pixel(x, y)
    return "%02X%02X%02X"%rgb



