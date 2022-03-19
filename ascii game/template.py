# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

i,x,y = 0,0,0
wall,char ="$","웃"   
xchar,ychar = 8,4
xborder, yborder = 16,8


list = [[8, 8, 8, 8, 8, 8], 
        [8, 2, 2, 2, 2, 8],
        [8, 2, 2, 2, 2, 8],
        [8, 2, 2, 2, 2, 8],
        [8, 2, 2, 2, 2, 8],
        [8, 8, 8, 8, 8, 8]] 

WIDTH = 1080
HEIGHT = 1920
FPS = 30



# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

'''class gmap(pygame.sprite.Sprite):
    def __init__(self):
        for y in range(0,6):
            for x in range(0,6):
                if map[x][y] == 1:
                    pygame.sprite.Sprite.__init__(self)
                    self.sprite = pygame.Surface(50,50)
                    self.image.fill(GREEN)
                    self.rect = self.image.get_rect()
                    self.rect.center = (x*50, y *50)
                    self.images.append(sprite) '''

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image = pygame.image.load("image/wall.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (x*50+25, y*50+25)


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
for y in range(0,6):
    for x in range(0,6):
        if list[x][y] == 8:
            tile = Tile(x, y)
            all_sprites.add(tile)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    
    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
