import random

while True:
    try:
        Temperature = float(input("Vad är dagens temperatur? "))
        break
    except:
        print("Skriv      \b\b\b\b\bbara ett tal tack.") #Trust me bro. It's important. I need these.

while True:
    Weather = input("Vad är dagens väder? ").lower()
    if "inte" in Weather.lower():
        print("Skriv inte \"inte\"!")
    else:
        break

if "snö" in Weather or Temperature < 0:
    Seed_Amount = random.randint(1, 10)

elif not("regn" in Weather) and Temperature < 20:
    Seed_Amount = 10
    print("Sjung en sång om livet till havs.")

elif "sol" in Weather and Temperature > 20:
    Seed_Amount = 5
    print("Berätta en rolig historia.")

elif "blås" in Weather or Temperature == 20:
    Seed_Amount = "inte"
    print("Sätt på radion")

while True:
    try:
        print(f"Ge {Seed_Amount} solrosfrön till Polly \u0D9E")
        break
    except:
        print("Polly är nöjd")
        break
