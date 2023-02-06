import text_game_basics as basics


basics.dialogue("dialogue.txt", 0, 4)

answer = input(">>").lower()

if answer == "no":
    pass

elif answer == "yes":
    while not False:
        pass  

basics.dialogue("game over\n:)")

