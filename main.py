from classe import *
width = 540
heigth = 400
cores = [255,255,255]
pg.init()
tela = pg.display.set_mode((width,heigth))
time = pg.time.Clock()
ball = Ball(tuple(cores))
player = Player(tuple(cores))
gol = Gol(tela.get_width())
j=0
t=1
_ = 2
txt = pg.font.SysFont('consolas',18,True)
texto = txt.render("Aperte q para sair ou r para repetir",1,tuple(cores))
rect_text = texto.get_rect()
rect_text.center = [200,10]

def reiniciar():
    global ball, player, gol, cores
    cores = [255,255,255]  
    ball = Ball(tuple(cores))
    player = Player(tuple(cores))
    gol = Gol(tela.get_width())   


while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            exit()
    pg.display.update()
    if ball.bateu == 1:
        tela.fill('black')
        tela.blit(texto,rect_text)
        tecla = pg.key.get_pressed()
        if tecla[pg.K_r]:
            reiniciar()
        elif tecla[pg.K_q]:
            print("END GAME")
            pg.quit()
            exit()
    else:
        tela.fill('black')
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