import pygame
from pygame.sprite import Sprite,Group
from Defines import *
class Square(Sprite):
    def __init__(self,color):
        Sprite.__init__(self)
        self.pic = color
        self.__x = -1
        self.__y = -1
    def get_x(self):
        return self.__x
    x = property(get_x)
    def get_y(self):
        return self.__y
    y = property(get_y)
    def get_pos(self):
        px = self.__x * SQUARE_SIZE
        py = (ROWS - self.__y - 1) * SQUARE_SIZE
        return (px,py)
    def draw(self,screen):
        screen.blit(self.pic,self.get_pos())
    def left(self):
        self.__x -= 1
    def right(self):
        self.__x += 1
    def down(self):
        self.__y -= 1
    def replace(self,x,y):
        if not (isinstance(x,int) and isinstance(y,int)):
            raise TypeError("x,y值必须是整数")
        self.__x = x
        self.__y = y
class Squares:
    def __init__(self,color,shapes,pic):
        self.pic = pic
        self.shapes = shapes
        self.index = 0
        self.shape = shapes[0]
        self.__x = -10
        self.__y = -10
        self.squares = Group()
        for pos in self.shape:
            self.squares.add(Square(color))
    def ready(self,screen):
        screen.blit(self.pic,PIC_POS)
    def start(self):
        self.__x = COLUMNS // 2
        self.__y = ROWS
        for pos,square in zip(self.shape,self.squares.sprites()):
            square.replace(self.__x + pos[0],self.__y + pos[1])
    @staticmethod
    def is_reliable(x,y,sqg):
        if x < 0 or x >= COLUMNS or y<0 or (x,y) in sqg.get_poses():
            return False
        else:
            return True
    def left(self,sqg):
        sqs = self.squares.sprites()
        for sq in sqs:
            if not self.is_reliable(sq.x - 1,sq.y,sqg):
                return False
        self.__x -= 1
        for sq in sqs:
            sq.left()
        return True
    def right(self,sqg):
        sqs = self.squares.sprites()
        for sq in sqs:
            if not self.is_reliable(sq.x + 1,sq.y,sqg):
                return False
        self.__x += 1
        for sq in sqs:
            sq.right()
        return True
    def down(self,sqg):
        sqs = self.squares.sprites()
        for sq in sqs:
            if not self.is_reliable(sq.x,sq.y - 1,sqg):
                return False
        self.__y -= 1
        for sq in sqs:
            sq.down()
        return True
    def change_shape(self,sqg):
        next_index = (self.index + 1) % len(self.shapes)
        next_shape = self.shapes[next_index]
        for pos in next_shape:
            if not self.is_reliable(self.__x + pos[0],self.__y + pos[1],sqg):
                return False
        self.index = next_index
        self.shape = next_shape
        for pos,square in zip(self.shape,self.squares.sprites()):
            square.replace(self.__x + pos[0],self.__y + pos[1])
        return True
    def draw(self,screen):
        for square in self.squares.sprites():
            square.draw(screen)
    def get_squares(self):
        return self.squares.sprites()
class SquareGroup:
    def __init__(self):
        self.squares = Group()
    def extend(self,sqs):
        for sq in sqs.get_squares():
            self.squares.add(sq)
    def clean(self):
        rows = 0
        for i in range(ROWS):
            if self.is_full_row(i-rows):
                self.clean_row(i-rows)
                rows += 1
        return rows
    def is_full_row(self,row):
        poses = self.get_poses()
        for col in range(COLUMNS):
            if (col,row) not in poses:
                return False
        return True
    def clean_row(self,row):
        del_s = []
        for sq in self.squares.sprites():
            if sq.y == row:
                del_s.append(sq)
            elif sq.y > row:
                sq.down()
        self.squares.remove(del_s)
    def get_poses(self):
        return tuple([(sq.x,sq.y) for sq in self.squares.sprites()])
    def draw(self,screen):
        for sq in self.squares.sprites():
            sq.draw(screen)
