import pygame
from utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = "freesansbold.ttf"
black_color = {0, 0, 0}
def get_score_elemen(points):
    font = pygame.font.Font(FONT_STYLE, 22)

    text = font.render("Points:" + str(points), True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (1000, 50)
    return text, text_rect

#def get_centered_message(message):
#    font = pygame.font.Font(FONT_STYLE, 22)
#    text = font.render("Message", True, black_color)

#    text_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
#    return text. text_rect

def get_centered_message(message, width = (SCREEN_WIDTH / 2), height = (SCREEN_HEIGHT / 2)):
    font = pygame.font.Font(FONT_STYLE, 22)
    text = font.render("message", True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text. text_rect



