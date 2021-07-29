# Importing the extensions
import pygame

# Initializing the pygame
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption('Asteroids')
icon = pygame.image.load('')

# Game Loop
running = True
while running:
    # Events
    for event in pygame.event.get():

        # Quitting
        if event.type == pygame.QUIT:
            running = False
