from classe import *
WIDTH = 540
HEIGTH = 400
cores = [255,255,255]
init()
tela = display.set_mode((WIDTH,HEIGTH))
time = time.Clock()
ball = Ball(tuple(cores))
player = Player(tuple(cores))
gol = Gol(tela.get_width())
j=0
t=1
_ = 2
txt = font.SysFont('consolas',18,True)
texto = txt.render("Aperte q para sair ou r para repetir",1,tuple(cores))
rect_text = texto.get_rect()
rect_text.center = [200,10]

def reiniciar():
    global ball, player, gol, cores
    cores = [255,255,255]
    ball = Ball(tuple(cores))
    player = Player(tuple(cores))
    gol = Gol(tela.get_width())   

def pontos():
    ponto = txt.render("Pontos: {}".format(ball.ponto),1,(255,255,255))
    return ponto

def get_rect_ponto():
    ponto = pontos()
    rect_ponto = ponto.get_rect()
    rect_ponto.center = [50,10]
    return rect_ponto

while True:
    for i in event.get():
        if i.type == QUIT:
            quit()
            exit()
    display.update()
    pontos()
    if ball.bateu == 1:
        tela.fill('black')
        tela.blit(texto,rect_text)
        tecla = key.get_pressed()
        if tecla[K_r]:
            reiniciar()
        elif tecla[K_q]:
            print("END GAME")
            quit()
            exit()
    else:
        tela.fill('black')
        tela.blit(pontos(),get_rect_ponto())
        player.update(tela)
        gol.update(tela)
        ball.update(player.rect,gol.rect,tela,tuple(cores))
        time.tick(60)
        if cores[j] <= 3:
            cores[j] = 255
        if cores[t] <= 5:
            cores[t] = 255
        if cores[_] <= 3:
            cores[_] = 255
        cores[j]-=5
        cores[t]-=4
        cores[_]-=2         
        player.set_color(tuple(cores))