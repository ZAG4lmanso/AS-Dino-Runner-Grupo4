from asyncio import IocpProactor
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
                self.obstacles.append(Cactus(SMALL_CACTUS))
                self.image_rect.y -= 20
                   

        for obstacle in self.obstacles:
            obstacle.update()
            
            #if obstacle.image_rect.x < -obstacle.image_rect.width:
             #   self.obstacles.pop()
            if game.dino.dino_rectcolliderect(obstacle.image_rect):
                pygame.time.delay(500)
                game.death_count +=1
                self.obstacles.cpop()
                if game.death_count == 5:
                    game.playing = False
                    print(game.death_count)
                break
            

            
