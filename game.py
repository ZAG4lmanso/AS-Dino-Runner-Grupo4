from cgitb import text
from distutils.core import run_setup
from doctest import master
from email import message
from multiprocessing.pool import RUN
import pygame
from utils.constants import BG, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from components.dinosaurio import Dinosaur
from components.obstacles.obstacle_manager import ObstacleManager
from utils import text_utils
from pygame import mixer

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_running = True
        self.dino = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.death_count = 0
        self.points = 0

    def new_method(self):
        self.obstacle_manager = ObstacleManager()

    def run(self):
        self.reset_attributes 
        # Game loop: events - update - draw
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
    
      

    def reset_attributes(self):
        self.playing = True
        self.death_count = 0
        self.points = 0
        

    def excute(self):
        while self.game_running:
            if not self.playing:
                self.show_menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.dino.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.score()
        self.draw_background()
        self.dino.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
            self.x_pos_bg -= self.game_speed
    
    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        text, text_rect = text_utils.get_score_element(self.points)
        self.screen .blit(text, text_rect)
        #print("Points:", self.points)   
        #print("Speed:", self.game_speed)
    

    
    def show_menu(self):
        self.screen.fill((255, 255, 0))
        self.show_menu_options()
        pygame.display.update()
        self.handle_events_menu()
        #pygame.time.delay(1000)
        #self.playing = True
        #self.run()
        
    def handle_events_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.run()
            if event.type == pygame.QUIT:
                self.game_running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()

    def show_menu_option(self):
        message = 'Welcome to Dino runner game' if self.death_count <= 0 else "Game over"
        text, text_rect = text_utils.get_centered_message(message, font_size=30)
        self.screen.blit(text, text_rect)
       
        pos_y = (SCREEN_HEIGHT / 2) + 20
        messege_instruction  = 'Press any key to start the game' 
        text_instruction, text_instruction_rect = text_utils.get_centered_message(messege_instruction, height=pos_y)
        self.screen.blit(text_instruction, text_instruction_rect)

        self.blit(RUNNING[0], ((SCREEN_WIDTH / 2), pos_y - 150))
        