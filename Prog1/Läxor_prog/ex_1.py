

def function_1(answer):
    answer += " Crazy"
    return answer

def function_2(answer):
    """This function does absolutely fucking nothing!"""
    print(f"({answer})/2")

def function_3(answer):
    answer.replace("no", "yes")
    return answer

def function_4(answer):
    answer.replace("yes", "no")
    return answer

while True:

    print("välj menyitem:\n1: skriv ut 1*1\n2: dela din string på två\n3: byt ut no med yes\n4: byt ut yes med no")
    answer = input(">>")

    if answer == "1":
        print(function_1(answer))

    elif answer == "2":
        print(function_2(answer))

    elif answer == "3":
        print(function_3(answer))

    elif answer == "4":
        print(function_4(answer))

    elif answer == "5":
        break
    
    else: print("vad gör du?")



