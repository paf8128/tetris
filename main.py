import pygame
from Defines import *
from Tools import Tools
def run_game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("俄罗斯方块 by paf")
    tools = Tools()
    while True:
        if not tools.check_event():
            break
        tools.update(screen)
    pygame.quit()
run_game()
