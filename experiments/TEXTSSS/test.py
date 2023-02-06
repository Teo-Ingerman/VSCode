import time, pygame, ctypes

def setup():
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    screen = pygame.display.set_mode(screensize)
    
    return screen

screen = setup()

class sentity():
    #TODO: lägg till image, image_size
    def __init__(self, collision_size, position):
        self.surface = pygame.surface.Surface(collision_size)
        self.position = position
        


pushable_rock = sentity((400, 400), (500, 500))


running = True

while running:
    screen.fill((0, 128, 0))
    
    screen.blit(pushable_rock.surface, pushable_rock.position)
    
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
                running = False
        
    
    pygame.display.update()