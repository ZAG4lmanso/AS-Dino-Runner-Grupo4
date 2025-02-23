



from pygame.sprite import Sprite
from email.mime import image
from utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):
    def __init__(self, image, type):
        self. image = image
        self.type = type
        self.image_rect = self.image[self, type].get_rect()
        self.image_rect.x = SCREEN_WIDTH
    
    def draw(self, screen):
        screen.blit(self.image[self, type], self.image_rect)
    
    def update(self, game):
        self.image_rect.x = game


