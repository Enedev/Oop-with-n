import pygame
 
STARTING_BLUE_BLOBS = 5
STARTING_RED_BLOBS = 2
 
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255,215,0)
 
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Square World")
clock = pygame.time.Clock()