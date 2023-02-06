#import random
#from typing import Text
#f = open("Funny_Jokes.txt")
#Text = f.readline().splitlines()
#print(random.choice(Text))

List_Test = ["\"Funny\"", "\"Lame\""]
import random
with open("Funny_Jokes_2.txt","r") as file:
    Lines = file.read().splitlines()
    print(random.choice(Lines))