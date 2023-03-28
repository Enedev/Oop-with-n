import pygame
from blobClass import Blob
from game_display import *


def draw_environment(blob_list):
    game_display.fill(WHITE)
 
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.rect(game_display, blob.color, [blob.x,blob.x,blob.y,blob.y], blob.size)
            blob.move()
 
    pygame.display.update()
    
def main():
    blue_blobs = dict(enumerate([Blob(BLUE) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([Blob(RED) for i in range(STARTING_RED_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment([blue_blobs,red_blobs])
        clock.tick(60)