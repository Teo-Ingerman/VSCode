import pyautogui, pynput, keyboard
import ctypes, platform, time
""" 
if platform.system() == 'Windows':
    Active_W = ctypes.windll.user32.GetActiveWindow()
    ctypes.windll.user32.SetWindowPos(Active_W,0,0,0,0,0,0x0002|0x0001)
 """
time.sleep(5)
pyautogui.moveTo(959, 359)

mouse = pynput.mouse.Controller()

# Click both left and right mouse buttons simultaneously
mouse.press(pynput.mouse.Button.left)
running = True
while running:
    if keyboard.is_pressed("q"):
        running = False
    for x in range(600):
        if keyboard.is_pressed("q"):
            break
        running = False
        pyautogui.moveTo(959, 359 - x)
        print(959, 359 - x)
    
    pyautogui.moveTo(959, 359)
        