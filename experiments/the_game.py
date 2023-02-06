import random, pygame




# initialize pygame
pygame.init()

#Screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Title and Icon
pygame.display.set_caption("Kitchen Nightmares")
icon = pygame.image.load("daver.png")
pygame.display.set_icon(icon)

running = True

player_image_1 = pygame.image.load("hugo_icon_1.png")

player_image_2 = pygame.image.load("hugo_icon_2.png")
# player scale, position and speed


player_scale_x = 64 
player_scale_y = 64
player_scale = (player_scale_x, player_scale_y)

player_image_1 = pygame.transform.scale(player_image_1, (player_scale))

player_image_2 = pygame.transform.scale(player_image_2, (player_scale))

player_images = [player_image_1, player_image_2]


player_x = 370
player_y = 480

player_x_speed = 0
player_y_speed = 0


#tree position and image loading

tree_image = pygame.image.load("tree.png")

tree_x = 400
tree_y = 400

#enemy class

class enemy():
    def __init__(self, health, speed, image):
        
        self.health = health
        self.speed = speed
        self.image =image
        

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


def animation(images, x, y):
    image = random.choice(images)
    screen.blit(image, (x, y))
    pass

while running:
    screen.fill((0, 128, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_x_speed = -0.8
            
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_x_speed = 0.8
            
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player_y_speed = -0.8
            
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player_y_speed = 0.8
            
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

    
    object_collision(tree_image, tree_x, tree_y, player_scale)
    

    #rendering player and objects
    animation(player_images, player_x, player_y)
    object_render(tree_x, tree_y)
    pygame.display.update()

pygame.quit()