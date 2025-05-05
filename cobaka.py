import pygame as pg
import nastroici

class Cobaka:
    def __init__(self):
        self.cartinca=pg.image.load("images/dog.png")
        self.cartinca=pg.transform.scale(self.cartinca,[250,250])
        self.pramougol=pg.rect.Rect([320,200],self.cartinca.get_size())
    def otrisovca(self,screen):
        screen.blit(self.cartinca,self.pramougol)
class Minicobaka:
    def __init__(self):
        self.cartinca=pg.image.load("images/dog.png")
        self.cartinca=pg.transform.scale(self.cartinca,[100,100])
        self.pramougol=pg.rect.Rect([320,400],self.cartinca.get_size())
        self.pramougol2=pg.rect.Rect([self.pramougol.x,self.pramougol.y],[self.pramougol.width/2,self.pramougol.height/2])
    def otrisovca(self,screen):
        screen.blit(self.cartinca,self.pramougol)
    def dvizjenie(self):
        clavishi=pg.key.get_pressed()
        if clavishi[pg.K_LEFT]==True and self.pramougol.x>100:
            self.pramougol.x=self.pramougol.x-3
        if clavishi[pg.K_RIGHT]==True and self.pramougol.right<800:
            self.pramougol.x=self.pramougol.x+3
        self.pramougol2.centerx=self.pramougol.centerx
        self.pramougol2.centery=self.pramougol.centery

