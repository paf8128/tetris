import pygame
from random import choice
from Square import *
from ViewManager import *
from Defines import *

class Tools:
    def __init__(self):
        self.timer = pygame.time.Clock()
        self.view_manager = ViewManager()
        self.back = self.view_manager.map
        self.stage = STAGE_START
    def start_game(self):
        self.pause = False
        self.stage = STAGE_GAME
        self.score = 0
        self.speed = SPEED
        self.fast = 1
        self.count = 0
        self.back = self.view_manager.map
        self.sqg = SquareGroup()
        self.sq = Squares(choice(self.view_manager.colors),\
                          *choice(self.view_manager.types))
        self.sq.start()
        self.next_sq = Squares(choice(self.view_manager.colors),\
                          *choice(self.view_manager.types))
    def draw_msg(self,screen,msg):
        text = self.view_manager.font_msg.render(msg,True,(255,0,0))
        draw_x = (screen.get_width() - text.get_width())//2
        screen.blit(text,(draw_x,0))
    def draw_score(self,screen,score):
        text = self.view_manager.font_score.render(str(score),True,(0,0,0))
        screen.blit(text,SCORE_POS)
    def have_failed(self,sqg):
        for pos in sqg.get_poses():
            if pos[1] >= ROWS:
                return True
        return False
    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if self.stage == STAGE_GAME:
                    if event.key == pygame.K_p:
                        self.pause = not self.pause
                    if event.key == pygame.K_LEFT and not self.pause:
                        if not self.sq.left(self.sqg):
                            self.view_manager.sounds[1].play()
                    if event.key == pygame.K_RIGHT and not self.pause:
                        if not self.sq.right(self.sqg):
                            self.view_manager.sounds[1].play()
                    if event.key == pygame.K_UP and not self.pause:
                        if not self.sq.change_shape(self.sqg):
                            self.view_manager.sounds[1].play()
                    if event.key == pygame.K_DOWN and not self.pause:
                        self.fast = FAST
                else:
                    if event.key == pygame.K_F1:
                        self.start_game()
            if event.type == pygame.KEYUP and self.stage == STAGE_GAME:
                if event.key == pygame.K_DOWN and not self.pause:
                    self.fast = 1
        return True
    def update(self,screen):
        fail = False
        screen.blit(self.back,(0,0))
        if self.stage == STAGE_START:
            self.draw_msg(screen,START_STR)
        elif self.stage == STAGE_GAME:
            if not self.pause:
                self.count += 1
                if self.count >= (self.speed//self.fast):
                    self.count -= self.speed//self.fast
                    if not self.sq.down(self.sqg):
                        self.sqg.extend(self.sq)
                        rows = self.sqg.clean()
                        if rows:
                            self.score += self.get_score(rows)
                            self.view_manager.sounds[0].play()
                            self.speed = max(SPEED - self.score//SPEED2,MIN_S)
                        if self.have_failed(self.sqg):
                            fail = True
                            self.stage = STAGE_LOSE
                        self.sq = self.next_sq
                        self.sq.start()
                        self.next_sq = Squares(choice(self.view_manager.colors)\
                          ,*choice(self.view_manager.types))
            self.sqg.draw(screen)
            self.sq.draw(screen)
            self.next_sq.ready(screen)
            self.draw_score(screen,self.score)
            if self.pause:
                self.draw_msg(screen,"游戏暂停")
        else:
            self.draw_msg(screen,LOSE_STR)
        pygame.display.update()
        if fail:
            self.back = screen.copy()
        self.timer.tick(60)
    @staticmethod
    def get_score(rows):
        return rows*(rows+1)//2
        
        
