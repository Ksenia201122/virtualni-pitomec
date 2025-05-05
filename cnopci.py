import pygame as pg
import pygame.freetype
import cartinci

class Cnopci:
    def __init__(self,x,y,cartinca,nadpis):
        self.cartinca=cartinca
        self.vremzcl=0
        self.pramougol=pg.rect.Rect([x,y],self.cartinca.get_size())
        self.shrift=pygame.freetype.Font("Breeze Normal.Ttf",40)
        self.nadpis=nadpis
        self.cartinipram=self.shrift.render(self.nadpis)
        self.cartinatext=self.cartinipram[0]
        self.pramougtext=self.cartinipram[1]
        self.pramougtext.center=self.pramougol.center
    def otrisovca(self,screen):
        screen.blit(self.cartinca,self.pramougol)
        screen.blit(self.cartinatext,self.pramougtext)
        tecvrem=pg.time.get_ticks()
        if tecvrem-self.vremzcl>200:
            self.cartinca=cartinci.cartincacnop
    def clic(self):
        self.cartinca=cartinci.najata
        self.vremzcl=pg.time.get_ticks()



