import time, winsound, os

def speech(file, delay_1, delay_2, list_index_start, list_index_end):
    with open(file) as file_open:
        list = file_open.read().splitlines()
        for x in list[list_index_start: list_index_end]:
            for y in x:
                print(y, end="", flush = True)
                time.sleep(delay_1)
            time.sleep(delay_2)
            print("")

def speech_name(file, delay_1, delay_2, name):
    with open(file) as file_open:
        list = file_open.read().splitlines()
        for x in list:
            if "[name]" in x:
                x = x.replace("[name]", name)
            for y in x:
                print(y, end="", flush = True)
                time.sleep(delay_1)
            time.sleep(delay_2)
            print("")

def speech_sound(text, delay, sound_clip):
    file_directory = os.getcwd()
    for x in text:
        winsound.PlaySound(f"{file_directory}\{sound_clip}", winsound.SND_FILENAME|winsound.SND_NOWAIT)
        print(x, end="", flush = True)
        time.sleep(delay)
    print("")
