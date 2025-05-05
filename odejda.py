import pygame as pg

class Odejda:
    def __init__(self,cartinca,x,y,cena,cuplena,nadeta):
        self.cartinca=cartinca
        self.cuplena=cuplena
        self.nadeta=nadeta
        self.cena=cena
        self.pramougol=pg.rect.Rect([x,y],self.cartinca.get_size())
    def otrisovca(self,screen):
        screen.blit(self.cartinca,self.pramougol)
