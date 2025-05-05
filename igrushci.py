import pygame as pg
import random
import cartinci

class Igrushci:
    def __init__(self): 
        self.cartinca=cartinci.spisoccarigrush[random.randint(0,2)]
        self.scorost=3
        self.scorostx=random.randint(1,5)
        self.scorosty=random.randint(1,5)
        self.pramougol=pg.rect.Rect([random.randint(100,800),0],self.cartinca.get_size())
        self.pramougol2=pg.rect.Rect([self.pramougol.x,self.pramougol.y],[self.pramougol.width/2,self.pramougol.height/2])
    def draw(self,screen):
        screen.blit(self.cartinca,self.pramougol)
    def dvizjenie(self):
        self.pramougol.y=self.pramougol.y+self.scorosty
        self.pramougol2.centerx=self.pramougol.centerx
        self.pramougol2.centery=self.pramougol.centery