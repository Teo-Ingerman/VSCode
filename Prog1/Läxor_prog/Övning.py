import random
Color_One = input("Favorite color: ")
Color_Two = input("second-favorite color: ")
Color_Three = input("third-favorite color: ")
Alien_Color = [Color_One, Color_Two, Color_Three]
Alien = random.choice(Alien_Color)
Total_Points = 0
if Alien == "Blue":
    Total_Points += 10
elif Alien == "Yellow":
    Total_Points += 5
elif Alien == "Pink":
    Total_Points += 15
print("Your alien is", Alien + "!")
