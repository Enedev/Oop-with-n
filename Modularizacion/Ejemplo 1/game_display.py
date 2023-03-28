import pygame
 
STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3
 
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255,215,0)
 
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()