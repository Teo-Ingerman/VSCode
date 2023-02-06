import PySimpleGUI as sg, winsound, ctypes, os, webbrowser, text_game_basics as basics


sg.theme("DarkAmber") 

layout_main = [[sg.Text("Choose your function")],
            [sg.Button("print some text")],
            [sg.Button("change your wallpaper")],
            [sg.Button("play some music")],
            [sg.Button("Open up a browser window")],
            [sg.Button("Quit program")]]


window_main = sg.Window("The function thing", layout_main)

def function_1():
    basics.dialogue("This is som text in the terminal")

def function_2():
    path = f"{os.getcwd()}/map_of_bird_failiures.jpg"   
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)

def function_3():
    winsound.PlaySound("mr_mason_jazz.wav", winsound.SND_FILENAME|winsound.SND_NOWAIT)

def function_4():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

while True:

    event, values = window_main.read()

    if event == sg.WIN_CLOSED:
        window_main.close()
        break

    elif event == "print some text":
        function_1()

    elif event == "change your wallpaper":
        function_2()

    elif event == "play some music":
        function_3()

    elif event == "Open up a browser window":
        function_4()

    elif event == "Quit program":
        window_main.close()
        break

