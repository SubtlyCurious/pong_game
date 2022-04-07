import pygame

#Initialize Game
pygame.init()
screen = width, height = 1500, 900
display = pygame.display.set_mode(screen)

game_on = True

while game_on:
    screen.fill((255,225, 226))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_on =False
    
    pygame.display.update()

    