import pygame

print(pygame.KEYDOWN)
pygame.init()


def input_change():
    
    while True:
        for event in pygame.event.get():
            print("h")
            if event.type == pygame.KEYDOWN:

                print(event.key)
                break
                
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
                
        if event.type == pygame.KEYDOWN:

            print(event.key)
            break