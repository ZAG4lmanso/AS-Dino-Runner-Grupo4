from email.mime import image
import imp
from multiprocessing import set_forkserver_preload
import pygame
from pygame.sprite import Sprite
from utils.constants import SCREEN_WIDTH
class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.image_rect = self.image[self.type].get_rect()
        self.image_rect.x = SCREEN_WIDTH
    
    def draw(self,screen):
        screen.blit(self.image[self.type],self.image_rect)
    
    def update(self):
        self.image_rect.x -= 20
        


