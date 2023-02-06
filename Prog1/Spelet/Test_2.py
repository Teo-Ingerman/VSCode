import random, os, winsound, PySimpleGUI as sg, time, threading, pygame
from turtle import title

# initialize pygame
pygame.init()

#Screen
screen = pygame.display.set_mode((800, 600)) #pygame.FULLSCREEN)

# TItel and ICon
pygame.display.set_caption("Kitchen Nightmares")
icon = pygame.image.load("kitchen_nightmares_icon_2.png")
pygame.display.set_icon(icon)


player_image = pygame.image.load("player.png")

player_position_x = 370
player_position_y = 480
player_position_x_speed = 0
player_position_y_speed = 0

enemy_image = pygame.image.load("enemy.png")

enemy_position_x = random.randint(0, 740)
enemy_position_y = random.randint(50, 150)
enemy_position_x_speed = 0
enemy_position_y_speed = 0



def player(x, y):
    screen.blit(player_image, (x, y))

def enemy(x, y):
    screen.blit(enemy_image, (x, y))

# Window loop
running = True
while running:
    screen.fill((0, 128, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_position_x_speed = -0.4
            
            if event.key == pygame.K_RIGHT:
                player_position_x_speed = 0.4
            
            if event.key == pygame.K_UP:
                player_position_y_speed = -0.4
            
            if event.key == pygame.K_DOWN:
                player_position_y_speed = 0.4
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_position_x_speed = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_position_y_speed = 0  
    player_position_x += player_position_x_speed
    player_position_y += player_position_y_speed
    
    
    if player_position_x <= 0:
        player_position_x = 0
    elif player_position_x >= 740:
        player_position_x = 740
    
    
    
    player(player_position_x, player_position_y)
    enemy(enemy_position_x, enemy_position_y)
    pygame.display.update()

pygame.quit()
