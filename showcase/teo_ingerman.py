

if __name__ != "__main__":
    print("this is not a module, don't import")
    quit()



import pygame, ctypes, os
import pygame_functions as pyf



pygame.init()

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)

def update_fps():
	fps = str(round(clock.get_fps(), 1))
	fps_text = font.render(fps, 1, pygame.Color("black"))
	return fps_text

save_check_folder = os.listdir()

#kollar vilka sparfiler som finns och väljer ett id som ingen har
i = 1
for x in save_check_folder:
    if "save" in x and "txt" in x:
        i += 1
save_id = i
    
#sätter storleken på skämen till datorns skärmstorlek
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

screen = pygame.display.set_mode(screensize)


image_scale = (128, 128)

enviroment_objects_folders = os.listdir("enviromental_objects/")
os.chdir("enviromental_objects/")
enviromental_objects_id = []


for folder in enviroment_objects_folders:
    enviromental_objects_id.append(os.listdir(folder))
    

enviromental_objects_loaded =[[], [], [], []]

#laddar alla bilder till en surface i förväg för att hjläpa programmet att köra snabbare
i = 0
for folder in enviromental_objects_id:
    for image in folder:
        entity_image = pygame.image.load(f"{os.getcwd()}\{enviroment_objects_folders[i]}\{image}").convert_alpha()
        entity_image = pygame.transform.scale(entity_image, image_scale)
        enviromental_objects_loaded[i].append(entity_image)
    i += 1


entity_id = 0
entity_type = 0
image_surface = ""
entities_placed = pygame.sprite.Group()
entity_list = []
os.chdir("../")


image_surface, image_scale, entity_type, entity_id = pyf.image_change(0, enviromental_objects_id, entity_type, entity_id, enviromental_objects_loaded)

running = True





while running:

    screen.fill((0, 128, 0))


    mouse_x, mouse_y = pygame.mouse.get_pos()

    mouse_button_pressed = pygame.mouse.get_pressed()
    
    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif mouse_button_pressed[0]:
                #lägger till en "tile" i en spritegroup nör man vänsterklickar
                try:
                    tile = pyf.entity_sprites(mouse_x - (image_scale[0]/2), mouse_y - (image_scale[1]/2), image_surface)
                    entities_placed.add(tile)
                    entity_object = pyf.entity_list_creator(entity_type, entity_id, (mouse_x, mouse_y), image_scale)
                    entity = [entity_object.type, entity_object.id, entity_object.pos, entity_object.scale]
                    entity_list.append(entity)
                except:
                    pass
                
            
            elif mouse_button_pressed[2]:
                
                #tar bort den "tilen" som musen är ovanför när man högerklickar
                i = 1
                for entities in reversed(list(entities_placed)):
                    click_rect = pygame.Rect(entities.rect)
                    if click_rect.collidepoint((mouse_x, mouse_y)):
                        entities.die()
                        entity_list.pop(-i)
                        break
                    i += 1


            elif event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    #forward scrolling
                    try:
                        image_surface, image_scale, entity_type, entity_id = pyf.image_change(entity_type, enviromental_objects_id, entity_type, entity_id, enviromental_objects_loaded, 1)
                    except:
                        pass

                elif event.y < 0:
                    #backward scrolling
                    try:
                        image_surface, image_scale, entity_type, entity_id = pyf.image_change(entity_type, enviromental_objects_id, entity_type, entity_id, enviromental_objects_loaded, -1)
                    except:
                        pass
                
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q:
                    image_surface, image_scale, entity_type, entity_id = pyf.image_change(0, enviromental_objects_id, entity_type, entity_id, enviromental_objects_loaded)

                elif event.key == pygame.K_w:
                    image_surface, image_scale, entity_type, entity_id = pyf.image_change(1, enviromental_objects_id, entity_type, entity_id, enviromental_objects_loaded)

                elif event.key == pygame.K_a:
                    image_surface, image_scale, entity_type, entity_id = pyf.image_change(2, enviromental_objects_id, entity_type, entity_id, enviromental_objects_loaded)
   
                elif event.key == pygame.K_s:
                    image_surface, image_scale, entity_type, entity_id = pyf.image_change(3, enviromental_objects_id, entity_type, entity_id, enviromental_objects_loaded)


                elif event.key == pygame.K_LCTRL:
                    image_surface, image_scale = pyf.transform(1, image_scale, enviromental_objects_loaded, entity_type, entity_id)

                elif event.key == pygame.K_LSHIFT:
                    image_surface, image_scale = pyf.transform(-1, image_scale, enviromental_objects_loaded, entity_type, entity_id)


                elif event.key == pygame.K_ESCAPE:
                    image_surface = ""

                elif event.key == pygame.K_RETURN:
                    pyf.save_entites(entity_list, save_id)

                if event.key == pygame.K_BACKSPACE:

                    mods = pygame.key.get_mods()

                    if mods & pygame.KMOD_ALT:
                        entities_placed.empty()


    try:
        entities_placed.draw(screen)
    except:
        pass

    pyf.image_surface_blit(image_surface, screen, image_scale, (mouse_x, mouse_y))

    screen.blit(update_fps(), (10,0))
    clock.tick(60)
    pygame.display.update()