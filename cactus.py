from email.mime import image
from operator import ipow
from obstacles.obstacle import Obstacle
import random

class Cactus(Obstacle):
    def __init__(self, image, rect_y = 300):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.image_rect.y = rect_y
        

