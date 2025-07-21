from classe import *
width = 540
heigth = 400
pg.init()
tela = pg.display.set_mode((width,heigth))
player = Player((255,255,255))
time = pg.time.Clock()
ball = Ball((255,255,255))
gol = Gol(tela.get_width())
while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            exit()
    tela.fill('black')
    player.update(tela)
    gol.update(tela)
    ball.update(player.rect,gol.rect,tela)
    pg.display.update()
    time.tick(60)