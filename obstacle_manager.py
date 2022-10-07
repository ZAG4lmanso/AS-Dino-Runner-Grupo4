from asyncio import IocpProactor
from cgitb import small
import game
import pygame
from components.obstacles.cactus import Cactus
import random

from utils.constants import( 
    LARGE_CACTUS,
    SMALL_CACTUS,
    )

class ObstacleManager():
    def __init__(self):
        self.obstacles = []
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            self.obstacles.pop()
    
    def update(self, game):
        if len(self.obstacles) == 0:
            cactus_size = random.randint(1, 2)

            if cactus_size == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif cactus_size == 2:
                small_cactus = Cactus(SMALL_CACTUS, 320)
                #small_cactus.size = 320
                #small_cactus.image_rect.y = 320   
                self.obstacles.append(Cactus(small_cactus))
                
                   

        for obstacle in self.obstacles:
            obstacle.update()
            
            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.pop()
            if game.dino.dino_rectcolliderect(obstacle.image_rect):
                pygame.time.delay(500)
                game.death_count +=1
                self.obstacles.pop()
                if game.death_count == 5:
                    game.playing = False
                    print(game.death_count)
                break
            

            
