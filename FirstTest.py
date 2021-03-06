# Import the pygame module
import pygame
from pygame.constants import K_d

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 0))
        self.rect = self.surf.get_rect()

# Move the sprite based on user keypresses
def updated(self, pressed_keys):
    #print("YO")
    if pressed_keys[K_UP]:
        self.rect.move_ip(0, -5)
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0, 5)
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-5, 0)
    if pressed_keys[K_RIGHT]:
        self.rect.move_ip(5, 0)

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():

        if event.type == QUIT:
            running = False
        # Check for QUIT event. If QUIT, then set running to false.
        
        # Get all the keys currently pressed
        # Fill the screen with black
    screen.fill((0, 0, 0))

        # Draw the player on the screen
    screen.blit(player.surf, player.rect)

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_ESCAPE]: #LEFT ARROW
        running = False 
    updated(player, pressed_keys)

        # Update the display
    pygame.display.update()