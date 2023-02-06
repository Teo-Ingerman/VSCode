import pygame, ctypes
    
    
    
images_yes = ["character_1.png", "character_2.png", "character_3.png", "character_4.png"]
loaded = []
for x in images_yes:
     loaded.append(pygame.transform.scale(pygame.image.load(x), (64, 64)))
    

def setup():
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    screen = pygame.display.set_mode(screensize)
    
    return screen

screen = setup()

class kill_me_now():
    def __init__(self, images):
        self.iterable = 0
        self.images = images
        self.active_image = images[0]
    
    def animation(player):
        
        for i, image in enumerate(player.images):
            if player.iterable > len(player.images)*60:
                player.iterable = 0
            if player.iterable > i*60:
                player.active_image = image
            
        player.iterable += 1
        
        return player

player = kill_me_now(loaded)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
            
    player.animation()
    screen.fill((0, 255, 0))
    #print(player.iterable)
    screen.blit(player.active_image, (600, 600))
    
    pygame.display.update()
    
    