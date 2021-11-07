#main

import pygame
import os #so we can import other files

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

WHITE = (255, 255, 255) #Made it a variable for readability

FPS = 60 #Set hardcode framerate
VEL = 5 # Velocity at which spaceships move
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png')) #grabbing image from asset folder
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90) #scaled down size of spaceship!, then rotated to face each other

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window(red, yellow): #Red yellow variables are where current spaceships are
    WIN.fill(WHITE) #Background!
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) #drawing yellow spaceship on the window at coords x 300 y 100
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) #rectangle that represents the spaceship
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): #Gets a list of all different events occurring
            if event.type == pygame.QUIT: #if quit stop running
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]: #LEFT
            yellow.x -= VEL
        if keys_pressed[pygame.K_d]: #RIGHT
            yellow.x += VEL
        if keys_pressed[pygame.K_w]: #UP
            yellow.y -= VEL
        if keys_pressed[pygame.K_s]: #DOWN
            yellow.y += VEL

        if keys_pressed[pygame.K_LEFT]: #LEFT ARROW
            red.x -= VEL
        if keys_pressed[pygame.K_RIGHT]: #RIGHT ARROW
            red.x += VEL
        if keys_pressed[pygame.K_UP]: #UP ARROW
            red.y -= VEL
        if keys_pressed[pygame.K_DOWN]: #DOWN ARROW
            red.y += VEL

        #red.x +=1 #Updating red to move one x pixel per second
        draw_window(red, yellow)

    pygame.quit()

if __name__ == "__main__":
    main()