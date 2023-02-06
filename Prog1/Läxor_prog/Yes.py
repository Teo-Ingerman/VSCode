import os, random, winsound
def Second_Condition():
    Song_Randomizer = random.choice(os.listdir("Sea_Songs/"))
    os.chdir("Sea_Songs/")
    File_Directory = os.getcwd()
    os.chdir("..")
    with open(f"{File_Directory}\{Song_Randomizer}") as file:
        Lines = file.read()    
    print(f"Sjung denna sång:\n{Lines}")
    Sound_Clip = Song_Randomizer.replace("txt", "wav")
    winsound.PlaySound(f"{Sound_Clip}", winsound.SND_FILENAME|winsound.SND_NOWAIT)
    print(Sound_Clip)
def Yes():
	print("Sound_Clip")
Second_Condition()
Yes()