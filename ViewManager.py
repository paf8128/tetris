import pygame
class ViewManager:
    def __init__(self):
        #地图
        self.map = pygame.image.load("images/map.jpg")
        #颜色
        self.colors = []
        self.colors.append(\
            pygame.image.load("images/bluesquare.jpg"))
        self.colors.append(\
            pygame.image.load("images/greensquare.jpg"))
        self.colors.append(\
            pygame.image.load("images/yellowsquare.jpg"))
        self.colors.append(\
            pygame.image.load("images/redsquare.jpg"))
        #形状
        self.types = []
        tian = (((0,0),(0,1),(1,0),(1,1)),)
        tian_img = pygame.image.load("images/tiansqs.jpg")
        self.types.append((tian,tian_img))
        yi = (((0,0),(1,0),(2,0),(3,0)),((0,1),(0,2),(0,3),(0,4)))
        yi_img = pygame.image.load("images/yisqs.jpg")
        self.types.append((yi,yi_img))
        t = (((0,0),(1,0),(2,0),(1,1)),((0,0),(0,1),(0,2),(1,1)),\
             ((0,1),(1,1),(2,1),(1,0)),((1,0),(1,1),(1,2),(0,1)))
        t_img = pygame.image.load("images/tsqs.jpg")
        self.types.append((t,t_img))
        l1 = (((0,2),(0,1),(0,0),(1,0)),((0,0),(0,1),(1,1),(2,1)),\
             ((0,2),(1,2),(1,1),(1,0)),((0,0),(1,0),(2,0),(2,1)))
        l1_img = pygame.image.load("images/l1sqs.jpg")
        self.types.append((l1,l1_img))
        l2 = (((0,0),(1,0),(1,1),(1,2)),((0,1),(0,0),(1,0),(2,0)),\
              ((1,2),(0,2),(0,1),(0,0)),((0,1),(1,1),(2,1),(2,0)))
        l2_img = pygame.image.load("images/l2sqs.jpg")
        self.types.append((l2,l2_img))
        z1 = (((0,1),(1,1),(1,0),(2,0)),((0,0),(0,1),(1,1),(1,2)))
        z1_img = pygame.image.load("images/z1sqs.jpg")
        self.types.append((z1,z1_img))
        z2 = (((0,0),(1,0),(1,1),(2,1)),((1,0),(1,1),(0,1),(0,2)))
        z2_img = pygame.image.load("images/z2sqs.jpg")
        self.types.append((z2,z2_img))
        #声音
        self.sounds = []
        self.sounds.append(\
            pygame.mixer.Sound("sounds/add_score.wav"))
        self.sounds.append(\
            pygame.mixer.Sound("sounds/error.wav"))
        #字体
        self.font_msg = pygame.font.Font("C:/Windows/Fonts/simkai.ttf",30)
        self.font_score = pygame.font.Font("C:/Windows/Fonts/simkai.ttf",40)

