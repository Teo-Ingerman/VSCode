import random, os, winsound

while True:
    try:
        Temperature = float(input("Vad är dagens temperatur? "))
        if Temperature == 69:
            print("Nice")
            winsound.PlaySound("Amogus_Drip.wav", winsound.SND_FILENAME|winsound.SND_NOWAIT)
        break
    except:
        print("Skriv bara ett tal tack.")

while True:
    Weather = input("Vad är dagens väder? ").lower()
    if "inte" in Weather:
        print("Skriv inte \"inte\"!")
    else:
        break

if "snö" in Weather or Temperature < 0:
    Seed_Amount = random.randint(1, 10)
    def Second_Condition():
        pass

elif not("regn" in Weather) and Temperature < 20:
    Seed_Amount = 10
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

elif "sol" in Weather and Temperature > 20:
    Seed_Amount = 5
    def Second_Condition():
        print("Berätta en rolig historia.")
        with open("Funny_Jokes.txt","r") as file:
            Lines = file.read().splitlines()
        print(f"T.ex {random.choice(Lines)}")

elif "blås" in Weather or Temperature == 20:
    Seed_Amount = "inte"
    def Second_Condition():
        print("Sätt på radion")
        winsound.PlaySound("Mr_Mason_Jazz.wav", winsound.SND_FILENAME|winsound.SND_NOWAIT)

while True:
    try:
        print(f"Ge {Seed_Amount} solrosfrön till Polly.")
        Second_Condition()
        break
    except:
        print("Polly är nöjd")
        break