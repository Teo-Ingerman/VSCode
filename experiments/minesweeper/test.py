import pyautogui

pos = (911, 670)

pyautogui.moveTo(pos)

def getHex(rgb):
    return "%02X%02X%02X"%rgb

def check_color(pos):

    x,y = pos
    # bbox = (x,y,x+1,y+1)
    # im = ImageGrab.grab(bbox=bbox)
    # rgbim = im.convert("RGB")
    # r,g,b = rgbim.getpixel((0,0))
    r, g, b = pyautogui.pixel(x, y)
    return getHex((r,g,b))
 
yes = [1, 2, 3, 1, 1, 1, 2, 4]

print(list(set(yes)))


#pyautogui.mouseInfo()

print(check_color(pos))