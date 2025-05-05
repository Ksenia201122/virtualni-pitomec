import pygame as pg
import pygame.freetype

class Haracteristica:
    def __init__(self,x,y,cartinca,hislo):
        self.cartinca=cartinca
        self.shrift=pygame.freetype.Font("Breeze Normal.Ttf",40)
        self.hislo=hislo
        self.pramougol=pg.rect.Rect([x,y],self.cartinca.get_size())
    def otrisovca(self,screen):
        screen.blit(self.cartinca,self.pramougol)
        self.shrift.render_to(screen,[self.pramougol.x+120,self.pramougol.y+40],str(self.hislo))

