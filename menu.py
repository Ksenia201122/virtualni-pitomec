import cartinci
import pygame as pg
import eda
import cnopci
import random

class Menuedi:
    def __init__(self,igra):
        self.igra=igra
        self.indexedi=0
        self.cartinca=cartinci.menu
        self.spisocedi=[]
        self.cnopcavpered=cnopci.Cnopci(600,400,cartinci.cartincacnop,"Вперед")
        self.cnopcanazad=cnopci.Cnopci(100,400,cartinci.cartincacnop,"Назад")
        self.cnopcasiest=cnopci.Cnopci(340,400,cartinci.cartincacnop,"Сьесть")
        for cartinca in cartinci.spisoccartedi:
            edaob=eda.Eda(cartinca,340,200,random.randint(50,600))
            self.spisocedi.append(edaob)
    def draw(self):
        self.igra.screen.blit(cartinci.fon,[0,0])
        self.igra.screen.blit(self.cartinca,[0,0])
        self.spisocedi[self.indexedi].otrisovca(self.igra.screen)
        self.cnopcavpered.otrisovca(self.igra.screen)
        self.cnopcanazad.otrisovca(self.igra.screen)
        self.cnopcasiest.otrisovca(self.igra.screen)
        pg.display.flip()
    def update(self):
        pass
    def vpered(self):
        if self.indexedi<len(self.spisocedi)-1:
            self.indexedi=self.indexedi+1
    def nazad(self):
        if self.indexedi>0:
            self.indexedi=self.indexedi-1
    def siest(self):
        if self.spisocedi[self.indexedi].cena<self.igra.money.hislo:
            self.igra.satiety.hislo=self.igra.satiety.hislo+random.randint(1,10)
            self.igra.money.hislo=self.igra.money.hislo-self.spisocedi[self.indexedi].cena
    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_ESCAPE:
                    self.igra.menu=None
            if event.type==pg.MOUSEBUTTONDOWN:
                if self.cnopcavpered.pramougol.collidepoint(event.pos):
                    self.vpered()
                    self.cnopcavpered.clic()
                if self.cnopcanazad.pramougol.collidepoint(event.pos):
                    self.nazad()
                    self.cnopcanazad.clic()
                if self.cnopcasiest.pramougol.collidepoint(event.pos):
                    self.siest()
                    self.cnopcasiest.clic()
                 