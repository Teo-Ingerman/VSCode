import pygame, time

pygame.init()

screen = pygame.display.set_mode((1280, 720))


class fucking_hell():
    def __init__(self):
        self.iterable = 0
        self.line = 1
        self.temporary_string = ""
        self.done = False
        self.string_to_print = ""
        self.color = (255, 255, 255)

text_box_img = pygame.image.load("text_box.png")
text_box_x = 205.5
text_box_y = 500


font = pygame.font.Font(r"fonts\minkraft.ttf", 30)

text = fucking_hell()


text_x = 230
text_y = 550

whos_talking_x = 480
whos_talking_y = 510
whos_talking_color = (211, 211, 211)
name = text.line - 1

def show_text(x, y, text, reset_key=False):

    """reset_key == True --> reset text"""

    if reset_key:
        text.done == False
        text.temporary_string == ""
        text.line = 1
        text.string_to_print = ""
    else:
        
    
        if not text.done:
            with open("textfile.txt") as file:
                lines = file.read().splitlines()
                for i, letter in enumerate(lines[text.line]):
                    if text.iterable > len(lines[text.line])*10:
                        text.iterable = 0
                    if text.iterable == i*10:
                        text.temporary_string += letter
                        text.string_to_print += letter
                        print(text.string_to_print)
                #print(lines[text.line])
                #print(text.temporary_string)
                text.iterable += 1
                if lines[text.line] == text.temporary_string:
                    text.line += 1
                    text.temporary_string = ""
                    text.iterable = -1
                    text.string_to_print += ""
                    print("new line")

                    if text.line == len(lines):
                        
                        text.done = True
        text = font.render(text.string_to_print, True, text.color)
        screen.blit(text, (x, y))

        with open("textfile.txt") as file:
                lines = file.read().splitlines()
                whos_talking_name = lines[name]
        whos_talking = font.render(whos_talking_name, True, whos_talking_color)
        screen.blit(whos_talking, (whos_talking_x, whos_talking_y))
    #return text
        
        
"""
whos_talking_x = 205.5
whos_talking_y = 510
whos_talking_color = (211, 211, 211)
whos_talking_name = "Generic Character"

def show_whos_talking(x, y):
    whos_talking = font.render(whos_talking_name, True, whos_talking_color)
    screen.blit(whos_talking, (x, y))
"""

def text_box(x, y):
    screen.blit(text_box_img, (x, y))

running = True
while running: 

    screen.fill((0, 255, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            show_text(text_x, text_y, text, reset_key=True)
                

    text_box(text_box_x, text_box_y)

    #show_whos_talking(whos_talking_y, whos_talking_y)
    show_text(text_x, text_y, text)


    pygame.display.update()