import pygame as pg
from random import randint
class Player(pg.sprite.Sprite):
    def __init__(self, color):
        self.color = color
        self.rect = pg.Rect((170,20),(30,8))
    def update(self,surface):
        self.draw(surface)
        self.moviment()
    def moviment(self):
        key = pg.key.get_pressed()
        if key[pg.K_RIGHT] and self.rect.right<=540:
            self.rect.x+=2
        if key[pg.K_LEFT] and self.rect.left>=0:
            self.rect.x-=2
    def draw(self,surface):
        pg.draw.rect(surface,self.color,self.rect)
    def set_color(self,color:tuple):
        self.color = color

class Ball(pg.sprite.Sprite):
    def __init__(self, color):
        self.color = color
        x = randint(300,380)
        y = randint(300,390)
        self.circle = pg.Rect((x,y),(6,10))
        self.velocy_x = 2
        self.velocy_y = -2
    def update(self,rect,gol,surface,color):
        self.draw(surface)
        self.moviment(rect,gol,color)
    def moviment(self,rect,gol,color):
        if self.colision(rect,color):
            self.velocy_y*=-1
        if self.colision(gol,(0,0,0)):
            print("END GAME")
            pg.quit()
            exit()
        if self.circle.right >= 540 or self.circle.left <= 0:
            self.velocy_x*=-1
            self.set_color(color)
        if self.circle.top >= 400:
            self.velocy_y*=-1
            self.set_color(color)
        self.circle.x+=int(self.velocy_x)
        self.circle.y+=int(self.velocy_y)
    def draw(self,surface):
        pg.draw.circle(surface, self.color, self.circle.center, (self.circle.width+self.circle.height) // 2)
    def colision(self,rect2:pg.Rect,color):
        if self.circle.colliderect(rect2):
            self.set_color(color)
            return True
        return False
    def set_color(self,color:tuple):
        self.color = color

class Gol(pg.sprite.Sprite):
    def __init__(self,largura):
        self.rect = pg.Rect((0,0),(largura,1))
    def draw(self,surface):
        pg.draw.rect(surface,'black',self.rect)
    def update(self, surface):
        self.draw(surface)