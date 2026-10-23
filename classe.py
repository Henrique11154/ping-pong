from pygame import sprite,key,K_r,K_q,K_RIGHT,K_LEFT,event,Rect,color,font,display,time,draw,init,QUIT,quit,image
from random import randint

class Player(sprite.Sprite):
    def __init__(self, color):
        self.cor = color
        self.rect = Rect((250,20),(30,8))
    def update(self,surface):
        self.draw(surface)
        self.moviment()
    def moviment(self):
        chave = key.get_pressed()
        if chave[K_RIGHT] and self.rect.right<=540:
            self.rect.x+=3
        if chave[K_LEFT] and self.rect.left>=0:
            self.rect.x-=3
    def draw(self,surface):
        draw.rect(surface,self.cor,self.rect)
    def set_color(self,color:tuple):
        self.cor = color

class Ball(sprite.Sprite):
    def __init__(self, color):
        self.color = color
        x = randint(300,380)
        y = randint(300,390)
        self.circle = Rect((x,y),(6,10))
        self.velocy_x = 2
        self.velocy_y = -2
        self.bateu = 0
        self.ponto = 0
    def update(self,rect,gol,surface,color):
        self.draw(surface)
        self.moviment(rect,gol,color)
    def moviment(self,rect,gol,color):
        if self.colision(rect,color):
            self.velocy_y = (self.velocy_y*-1) +1
            self.ponto+=1
        if self.colision(gol,(0,0,0)):
            self.bateu = 1
            self.velocy_x = 0
            self.velocy_y = 0
        if self.circle.right >= 540 or self.circle.left <= 0:
            self.velocy_x*=-1
            self.set_color(color)
        if self.circle.bottom >= 400:
            self.velocy_y*=-1
            self.set_color(color)
        self.circle.x+=int(self.velocy_x)
        self.circle.y+=int(self.velocy_y)
    def draw(self,surface):
        draw.circle(surface, self.color, self.circle.center, (self.circle.width+self.circle.height) // 2)
    def colision(self,rect2:Rect,color):
        if self.circle.colliderect(rect2):
            self.set_color(color)
            return True
        return False
    def set_color(self,color:tuple):
        self.color = color

class Gol(sprite.Sprite):
    def __init__(self,largura):
        self.rect = Rect((0,0),(largura,1))
    def draw(self,surface):
        draw.rect(surface,'black',self.rect)
    def update(self, surface):
        self.draw(surface)
        