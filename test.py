import sys
import pygame
from pygame.locals import *
import time

pygame.init()

screen = pygame.display.set_mode((1600,1200))

pygame.display.set_caption("PyGame")
image = pygame.image.load("./Downloads/sample.jpg")

def main():
    while True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

                sys.exit
        screen.blit(image,(0,0))
        pygame.display.update()

main()