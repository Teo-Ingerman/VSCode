import pyautogui, keyboard, pynput, time


time.sleep(10)


mouse = pynput.mouse.Controller()

                # Click both left and right mouse buttons simultaneously
mouse.press(pynput.mouse.Button.left)

mouse.release(pynput.mouse.Button.left)


while True:
    if keyboard.is_pressed("l"):
        break
    #pyautogui.click()
    
    mouse.press(pynput.mouse.Button.left)

    mouse.release(pynput.mouse.Button.left)