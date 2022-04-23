# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import os


i,x,y = 0,0,0
wall,char ="$","웃"   
xchar,ychar = 1,1
xborder, yborder = 10,10
border = xborder
chartile = 0
maparray1 = []
speed = 0.001 
tilewidth = 50

for i in range(0,border+1):
    maparray2 = []
    for j in range(0,border+1):
        if i == 0 or i == border:
            maparray2.append(8)
        elif j == 0 or j == border:
            maparray2.append(8)
        else:
            maparray2.append(2)
    maparray1.append(maparray2)
        
list = [[8, 8, 8, 8, 8, 8], 
        [8, 2, 2, 2, 2, 8],
        [8, 2, 2, 2, 2, 8],
        [8, 2, 2, 2, 2, 8],
        [8, 2, 2, 2, 2, 8],
        [8, 8, 8, 8, 8, 8]] 

WIDTH = 1080
HEIGHT = 1920
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image = pygame.image.load("image/wall.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (x*50+25, y*50+25)

class Char(pygame.sprite.Sprite,):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image = pygame.image.load("image/rsz_kratos.gif").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (x*50+25, y*50+25)
        self.xend = xchar
        self.yend = ychar
    def update(self,dtime):
        if xchar != self.xend:
            self.rect.center = (self.rect.center[0]-tilewidth*speed*dtime, self.rect.center[1])
    def moveleft(self,x):
        global xchar, ychar
        if maparray1[xchar-1][ychar] != 8:    
            xend = xchar-1
            self.rect.center = (xchar*50+25, ychar*50+25)
        
    def moveright(self,x):
        global xchar,ychar
        if maparray1[xchar+1][ychar] != 8:
            xchar +=1
            self.rect.center = (xchar*50+25, ychar*50+25)

    def moveup(self,y):
        global xchar, ychar
        if maparray1[xchar][ychar-1] != 8:   
            ychar -=1
            self.rect.center = (xchar*50+25, ychar*50+25)
              
    def movedown(self,x):
        global xchar,ychar
        if maparray1[xchar][ychar+1] != 8:
            ychar +=1
            self.rect.center = (xchar*50+25, ychar*50+25)
    
            


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
for y in range(0,border+1):
    for x in range(0,border+1):
        if x == xchar and y == ychar:
            chartile = Char(x,y)
            all_sprites.add(chartile)
        if maparray1[x][y] == 8:
            tile = Tile(x, y)
            all_sprites.add(tile)




# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    chartile.update(1000/30)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in(pygame.K_a, pygame.K_LEFT):
                chartile.moveleft(xchar)
            if event.key in(pygame.K_d, pygame.K_RIGHT):
                chartile.moveright(xchar)
            if event.key in(pygame.K_w, pygame.K_UP):
                chartile.moveup(ychar)
            if event.key in(pygame.K_s, pygame.K_DOWN):
                chartile.movedown(ychar)
            if event.key == pygame.K_ESCAPE:
                running = False
    # Обновление
    
    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
