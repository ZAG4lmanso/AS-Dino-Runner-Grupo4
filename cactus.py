from email.mime import image
from operator import ipow
from components.obstacles.obstacle import Obstacle
import random

class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image)
        self.image_rect.y = 300
