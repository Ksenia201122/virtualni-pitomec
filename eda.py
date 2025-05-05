import pygame as pg
import pygame.freetype

class Eda:
    def __init__(self,cartinca,x,y,cena):
        self.cartinca=cartinca
        self.cena=cena
        self.shrift=pygame.freetype.Font("Breeze Normal.Ttf",30)
        self.pramougol=pg.rect.Rect([x,y],self.cartinca.get_size())
    def otrisovca(self,screen):
        screen.blit(self.cartinca,self.pramougol)
        self.shrift.render_to(screen,[430,170],str(self.cena))
