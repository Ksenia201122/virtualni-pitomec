import pygame as pg
import cartinci
import cobaka
import igrushci
import random
import pygame.freetype

class Miniigra:
    def __init__(self,igra):
        self.cartinca=cartinci.menuigri
        self.minicobaca=cobaka.Minicobaka()
        self.igrushca=igrushci.Igrushci()
        self.igra=igra
        self.shrift=pygame.freetype.Font("Breeze Normal.Ttf",40)
        self.igrushsob=pg.USEREVENT+3
        pg.time.set_timer(self.igrushsob,1000)
        self.spisocigrush=[]
        self.coligr=0
    def draw(self):
        self.igra.screen.blit(cartinci.fon,[0,0])
        self.igra.screen.blit(self.cartinca,[0,0])
        for igrushca in self.spisocigrush:
            igrushca.draw(self.igra.screen)
        self.minicobaca.otrisovca(self.igra.screen)
        self.shrift.render_to(self.igra.screen,[50,50],str(self.coligr))
        pg.display.flip()
    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_ESCAPE:
                    self.igra.menu=None
                    self.igra.happy.hislo=self.igra.happy.hislo+self.coligr
                    if self.igra.happy.hislo>100:
                        self.igra.happy.hislo=100
                    self.coligr=0
                    self.spisocigrush.clear()
            if event.type==self.igrushsob:
                igrushca=igrushci.Igrushci()
                self.spisocigrush.append(igrushca)
    def update(self):
        self.minicobaca.dvizjenie()
        for igrushca in self.spisocigrush:
            igrushca.dvizjenie()
            if self.minicobaca.pramougol2.colliderect(igrushca.pramougol2):
                self.coligr=self.coligr+1
                self.spisocigrush.remove(igrushca)
