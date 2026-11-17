from pygame import sprite,key,K_r,K_q,K_RIGHT,K_LEFT,event,Rect,color,font,display,time,draw,init,QUIT,quit,image
from random import randint

init()
class Player(sprite.Sprite):
    def __init__(self, color):
        self.cor = color
        self.rect = Rect((250,20),(30,8))
    def update(self,surface):
        self.draw(surface)
        self.moviment()
    def moviment(self):
        # Realiza o movimento do retangulo
        chave = key.get_pressed()
        if chave[K_RIGHT] and self.rect.right<=540:
            self.rect.x+=3
        if chave[K_LEFT] and self.rect.left>=0:
            self.rect.x-=3
    def draw(self,surface):
        # desenha o retangulo na tela
        draw.rect(surface,self.cor,self.rect)
    def set_color(self,color:tuple):
        self.cor = color

class Ball(sprite.Sprite):
    def __init__(self, color):
        # Inicia a bola em uma posição aleatoria
        # sua velocidade, se ela bateu no topo da tela
        # e pontuação a cada vez em que a bola bater no retangulo
        self.color = color
        x = randint(100,380)
        y = randint(300,380)
        self.circle = Rect((x,y),(12,20))
        self.velocy_x = 2
        self.velocy_y = randint(-2,2)
        self.bateu = 0
        self.ponto = 0
        self.safe_dist = 5
    def update(self,rect,gol,surface,color):
        self.draw(surface)
        self.moviment(rect,gol,color,surface)
    def moviment(self,rect,gol,color,surface):
        # Realiza a movementação da bola com base em que ela está colidindo
        if self.colision(rect,color):
            self.velocy_y = (self.velocy_y*-1) +0.7
            self.ponto+=1
        if self.colision(gol,(0,0,0)):
            self.bateu = 1
            self.velocy_x = 0
            self.velocy_y = 0
        if self.circle.right >= surface.get_width() or self.circle.left <= 0:
            self.velocy_x*=-1
            self.set_color(color)
        if self.circle.bottom >= surface.get_height():
            self.velocy_y*=-1
            self.set_color(color)
        if self.velocy_y == 0:
            self.velocy_y = randint(-2,2)
        self.circle.x+=int(self.velocy_x)
        self.circle.y+=int(self.velocy_y)
    def draw(self,surface):
        # Desenha um circulo na tela
        draw.circle(surface, self.color, self.circle.center, float((self.circle.width + self.circle.height)/4))
    def colision(self,rect2:Rect,color):
        # Verifica se o retangulo do circulo sobrepos outro retangulo
        if self.circle.colliderect(rect2):
            # Realiza os calculos para garantir uma colisão mais precisa
            # evita erros de colisão lateral
            cimaBaixo = self.circle.top - rect2.bottom
            esq_dir = self.circle.left - rect2.right
            dir_esq = rect2.left - self.circle.right
            if cimaBaixo < self.safe_dist and cimaBaixo > esq_dir and cimaBaixo > dir_esq:    
                self.set_color(color)
                return True
            if esq_dir < self.safe_dist and esq_dir > cimaBaixo:    
                self.set_color(color)
                self.velocy_x *= -1
                return True
            if dir_esq < self.safe_dist and dir_esq > cimaBaixo:    
                self.set_color(color)
                self.velocy_x *= -1
                return True
        return False
    def set_color(self,color:tuple):
        self.color = color

class Gol(sprite.Sprite):
    def __init__(self,largura):
        # Inicia Retangulo de colisão para fim de jogo
        self.rect = Rect((0,0),(largura,1))
    def draw(self,surface):
        # Desenha o retangulo na tela
        draw.rect(surface,'red',self.rect)
    def update(self, surface):
        self.draw(surface)
        