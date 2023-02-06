import pygame


#tar en bilds surface och bstämmer self.rect vilket behövs i en pygame sprite group 
class entity_sprites(pygame.sprite.Sprite): 
    def __init__(self, x, y, image_surface):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_surface
        self.rect = self.image.get_rect(x = x, y = y)

    def die(self):
        self.kill()

#skapar ett list id för varje placerat objekt som kommer att sparas i en txt fil
class entity_list_creator():
    def __init__(self, entity_type, entity_id, position, scale):
        self.type = entity_type
        self.id = entity_id
        self.pos = position
        self.scale = scale


#öppnar en sparfil eller skriver över den om sparfunktioner används flera gånger
def save_entites(entity_list, save_id):
    try:
        with open(f"position_save_{save_id}.txt", "w") as file:
            pass

        with open(f"position_save_{save_id}.txt", "a") as file:
            for entity in entity_list:
                file.write(f"{entity}")
                file.write("\n")
    except:
        pass

#ändrar vilken bild som visas under musen
def image_change(entity_type_change, enviromental_objects_id, entity_type, entity_id, enviromental_objects_loaded, change=0):

    entity_type = entity_type_change
    
    if change == 0:
        entity_id = 0
    else:
        entity_id += change

        if entity_id >= len(enviromental_objects_id[entity_type]):
            entity_id = len(enviromental_objects_id[entity_type]) - 1

        elif entity_id < 0:
            entity_id = 0

    image_surface = (enviromental_objects_loaded[entity_type])[entity_id]
    image_scale = (128, 128)
    return image_surface, image_scale, entity_type, entity_id


#minskar eller ökar storleken på önskad bild
def transform(change, image_scale, enviromental_objects_loaded, entity_type, entity_id):

    x_size, y_size = image_scale

    try:
        if x_size <= 256 and y_size <= 256 and x_size >= 32 and y_size >= 32:

            x_size -= (x_size//8)*change
            y_size -= (y_size//8)*change

            if x_size < 32:
                x_size = 32
                y_size = 32

            if x_size > 256:
                x_size = 256
                y_size = 256

            image_scale = (x_size, y_size)

            image_surface = pygame.transform.scale((enviromental_objects_loaded[entity_type])[entity_id], image_scale)
    except:
        pass

    return image_surface, image_scale


#blittar den aktiva bilden på skärmen med en offset så dens center hamnar rakt på musen
def image_surface_blit(image_surface, screen, image_scale, position):
    x, y = position
    try:
        screen.blit(image_surface, (x - (image_scale[0]/2), y - (image_scale[1]/2)))
    except:
        pass

