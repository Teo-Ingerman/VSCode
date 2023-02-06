import pygame, ctypes

try:
    import moviepy.editor
except:
    print("please install moviepy using the following command in command prompt:\npip install moviepy")
    quit()

pygame.init()

pygame.mixer.init()

running = True

video = moviepy.editor.VideoFileClip("loading_screen.mov")


first_button_pressed = False

starting_area = False

display_value = -1

display_id = "home screen"

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

video = video.resize(screensize)

player_scale_x = 64 
player_scale_y = 64
player_scale = (player_scale_x, player_scale_y)

player_image = pygame.image.load("hugo_icon_1.png")

player_image = pygame.transform.scale(player_image, (player_scale))


player_x = 370
player_y = 480

player_x_speed = 0
player_y_speed = 0

tree_image = pygame.image.load("tree.png")

tree_x = 400
tree_y = 400

screen = pygame.display.set_mode(screensize)

pygame.mixer.music.load("background_music.mp3")

pygame.mixer.music.play(loops=-1)

pygame.mixer.music.set_volume(0.2)

def display():
    global display_value
    global display_id
    
    if display_id == "home screen":
        if display_value == -1:
            image = "home_screen_start.png"

        elif display_value <= 1:
            image = "home_screen_start_select.png"
            display_value = 1

        elif display_value == 2:
            image = "home_screen_achivements_select.png"

        elif display_value == 3:
            image = "home_screen_options_select.png"

        elif display_value >= 4:
            image = "home_screen_quit_select.png"
            display_value = 4
    
    if display_id == "save files":

        if display_value <= 1:
            image = "save_files_one_select.png"
            display_value = 1

        if display_value == 2:
            image = "save_files_two_select.png"

        if display_value == 3:
            image = "save_files_three_select.png"

        if display_value >= 4:
            image = "save_files_back_select.png"
            display_value = 4

    if display_id == "quit check":
        if display_value <= 1:
            image = "quit_check_yes_select.png"
            display_value = 1

        if display_value >= 2:
            image = "quit_check_no_select.png"
            display_value = 2
    
    if display_id == "achivement page":
        image = "achivement_page.png"


    try: 
        image = pygame.image.load(image)
        image_scaled = pygame.transform.scale(image, screensize)
        screen.blit(image_scaled, (0, 0))
    
    except:
        pass

def object_collision(entity, entity_x, entity_y, player_scale):
    global player_x
    global player_y

    player_scale_x = player_scale[0]
    player_scale_y = player_scale[1]

    width, height = entity.get_size()

    # detection for collision from the right
    if player_x < entity_x + width and player_x > entity_x + (width / 2):
        #checks if player is interacting with the y axis
        if player_y > entity_y - player_scale_y and player_y < entity_y + height:
            player_x = entity_x + width

    # detection for collision from the left
    if player_x > entity_x - player_scale_x and player_x < entity_x + (width / 2) - player_scale_x:
        #checks if player is interacting with the y axis
        if player_y > entity_y - player_scale_y and player_y < entity_y + height:
            player_x = entity_x - player_scale_x

    # detection for collision from below
    if player_y < entity_y + height and player_y > entity_y + (height / 2):
        #checks if player is interacting with the x axis
        if player_x > entity_x - player_scale_x and player_x < entity_x + width:
            player_y = entity_y + height

    # detection for collision from above
    if player_y > entity_y - player_scale_y and player_y < entity_y + (height / 2) - player_scale_y:
        #checks if player is interacting with the x axis
        if player_x > entity_x - player_scale_x and player_x < entity_x + width:
            player_y = entity_y - player_scale_y

def object_render(x, y):
    screen.blit(tree_image, (x, y))


def animation(image, x, y):
    screen.blit(image, (x, y))



while running:
    screen.fill((0, 128, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not first_button_pressed:
            if event.type == pygame.KEYDOWN:
                first_button_pressed = True
                display_value = 1

        else:
            if event.type == pygame.KEYDOWN:
                if not starting_area:
                    if event.key == pygame.K_UP or event.key == pygame.K_w and (display_id != "quit check" and display_id != "starting area"):
                        display_value -= 1
                    
                    elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and display_id != "starting area":
                        display_value += 1

                    elif display_id == "quit check" and display_value == 1  and event.key == pygame.K_SPACE:
                        running = False
                    
                    elif display_id == "quit check" and display_value == 2  and event.key == pygame.K_SPACE:
                        display_id = "home screen"
                        display_value = -1

                    elif display_value == 1 and display_id == "home screen" and event.key == pygame.K_SPACE:
                        display_id = "save files"

                    elif display_value == 2 and display_id == "home screen" and event.key == pygame.K_SPACE:
                        display_id = "achivement page"

                    elif display_value == 4 and display_id == "home screen" and event.key == pygame.K_SPACE:
                        display_id = "quit check"
                        display_value = 2

                    elif display_value == 4 and display_id == "save files" and event.key == pygame.K_SPACE:
                        display_id = "home screen"
                        display_value = -1

                    elif display_id == "achivement page" and event.key == pygame.K_SPACE:
                        display_id = "home screen"
                        display_value = -1

                    elif display_id == "quit check" and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                        display_value -= 1

                    elif display_id == "quit check" and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                        display_value += 1

                    elif display_id == "save files" and display_value == 1 and event.key == pygame.K_SPACE:
                        display_id = "starting area"
                        starting_area = True
                        video.preview()
                else:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        player_x_speed = -0.8
                    
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player_x_speed = 0.8
                    
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        player_y_speed = -0.8
                    
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        player_y_speed = 0.8
                    
                    if event.key == pygame.K_ESCAPE:
                        starting_area = False
                        display_value = -1
                        display_id = "home screen"

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_speed = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_y_speed = 0 

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    player_x_speed = 0

                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player_y_speed = 0 

    player_x += player_x_speed
    player_y += player_y_speed            

    if display_id == "starting area":

        object_collision(tree_image, tree_x, tree_y, player_scale)
        #rendering player and objects
        animation(player_image, player_x, player_y)
        object_render(tree_x, tree_y)

    else:
        display()
    pygame.display.update()
