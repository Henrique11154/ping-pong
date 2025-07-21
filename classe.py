import pygame as pg
from random import randint
class Player(pg.sprite.Sprite):
    def __init__(self, color):
        self.color = color
        self.rect = pg.Rect((170,20),(25,5))
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


class Ball(pg.sprite.Sprite):
    def __init__(self, color):
        self.color = color
        x = randint(300,380)
        y = randint(300,390)
        self.circle = pg.Rect((x,y),(6,10))
        self.velocy_x = 1.5
        self.velocy_y = -1.5
    def update(self,rect,gol,surface):
        self.draw(surface)
        self.moviment(rect,gol)
    def moviment(self,rect,gol):
        if self.colision(rect):
            self.velocy_y*=-1
        if self.colision(gol):
            print("END GAME")
            pg.quit()
            exit
        if self.circle.centerx >= 540 or self.circle.right <= 0:
            self.velocy_x*=-1
        if self.circle.top >= 400:
            self.velocy_y*=-1
        self.circle.x+=self.velocy_x
        self.circle.y+=self.velocy_y
    def draw(self,surface):
        pg.draw.circle(surface,self.color,(self.circle.x,self.circle.y),(self.circle.height+self.circle.width)/2)
    def colision(self,rect2:pg.Rect):
        if self.circle.collidepoint(rect2.x,rect2.y):
            print('colide')
            return True
        return False

class Gol(pg.sprite.Sprite):
    def __init__(self,largura):
        self.rect = pg.Rect((0,0),(largura,1))
    def draw(self,surface):
        pg.draw.rect(surface,'black',self.rect)
    def update(self, surface):
        self.draw(surface)