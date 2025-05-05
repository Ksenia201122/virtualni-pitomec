import pygame as pg
import cartinci
import odejda
import cnopci
import random
import haracteristica

class Menuodejdi:
    def __init__(self,igra):
        self.igra=igra
        self.indexodejdi=0
        self.spisocodejdi=[]
        self.shrift=pg.freetype.Font("Breeze Normal.Ttf",40)
        self.cnopcavpered=cnopci.Cnopci(600,300,cartinci.cartincacnop,"Вперед")
        self.cnopcanazad=cnopci.Cnopci(600,400,cartinci.cartincacnop,"Назад")
        self.cnopcanadet=cnopci.Cnopci(100,300,cartinci.cartincacnop,"Надеть")
        self.cnopcacupit=cnopci.Cnopci(100,400,cartinci.cartincacnop,"Купить")
        self.cartinca=cartinci.menu
        fayl=open("cuplena","r",encoding="UTF-8")
        read=fayl.readlines()
        fayl.close()
        fayl=open("nadeta","r",encoding="utf-8")
        readnadeta=fayl.readlines()
        fayl.close()
        t=0
        for cartinca in cartinci.spisoccarodejdi:
            obodejdi=odejda.Odejda(cartinca,320,200,random.randint(50,500),read[t][0:-1],readnadeta[t][0:-1])
            t=t+1
            self.spisocodejdi.append(obodejdi)
    def draw(self):
        self.igra.screen.blit(cartinci.fon,[0,0])
        self.igra.screen.blit(self.cartinca,[0,0])
        self.spisocodejdi[self.indexodejdi].otrisovca(self.igra.screen)
        self.necuplena=self.cnopcavpered.otrisovca(self.igra.screen)
        self.cnopcanazad.otrisovca(self.igra.screen)
        self.cnopcanadet.otrisovca(self.igra.screen)
        self.cnopcacupit.otrisovca(self.igra.screen)
        if self.spisocodejdi[self.indexodejdi].cuplena=="Не куплена":
            self.shrift.render_to(self.igra.screen,[100,100],"Не куплена")
        else:
            self.shrift.render_to(self.igra.screen,[100,200],"Куплена")
        if self.spisocodejdi[self.indexodejdi].nadeta=="Не надета":
            self.shrift.render_to(self.igra.screen,[600,100],"Не надета")
        else:
            self.shrift.render_to(self.igra.screen,[600,200],"Надета")
        pg.display.flip()
    def update(self):
        pass
    def vpered(self):
        if self.indexodejdi<len(self.spisocodejdi)-1:
            self.indexodejdi=self.indexodejdi+1
    def nazad(self):
        if self.indexodejdi>0:
            self.indexodejdi=self.indexodejdi-1
    def cupit(self):
        if self.spisocodejdi[self.indexodejdi].cena<self.igra.money.hislo and self.spisocodejdi[self.indexodejdi].cuplena=="Не куплена":
            self.igra.money.hislo=self.igra.money.hislo-self.spisocodejdi[self.indexodejdi].cena
            self.spisocodejdi[self.indexodejdi].cuplena="Куплена" 
    def nadeta(self):
        if self.spisocodejdi[self.indexodejdi].cuplena=="Куплена":
            if self.spisocodejdi[self.indexodejdi].nadeta=="Надета":
                self.spisocodejdi[self.indexodejdi].nadeta="Не надета"
            else:
                self.spisocodejdi[self.indexodejdi].nadeta="Надета"
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
                if self.cnopcacupit.pramougol.collidepoint(event.pos):
                    self.cupit()
                    self.cnopcacupit.clic()
                if self.cnopcanadet.pramougol.collidepoint(event.pos):
                    self.nadeta()
                    self.cnopcanadet.clic()
                        
                    