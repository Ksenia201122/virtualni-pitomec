import pygame as pg
from nastroici import *
from cartinci import *
import haracteristica
import cobaka 
import cnopci
import menu
import menuodejdi
import random
import haracteristica
import menuigri
import igrushci
import pygame.freetype
# Инициализация pg
pg.init()

# Размеры окна


class Game:
    def __init__(self):

        # Создание окна
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.cobaka=cobaka.Cobaka()
        self.sostoanie="igra"
        file=open("haracteristica","r")
        read=file.readlines()
        moneti=int(read[0])
        happ=int(read[1])
        healt=int(read[3])
        satiet=int(read[2])
        file.close()
        fayl=open("ylutsh","r")
        read=fayl.readlines()
        ulytsh=int(read[0])
        self.happy=haracteristica.Haracteristica(50,50,happy,happ)
        self.health=haracteristica.Haracteristica(50,150,health,healt)
        self.satiety=haracteristica.Haracteristica(50,250,satiety,satiet)
        self.money=haracteristica.Haracteristica(50,350,money,moneti)
        self.cnopca1=cnopci.Cnopci(650,150,cartincacnop,"Еда")
        self.cnopca2=cnopci.Cnopci(650,250,cartincacnop2,"Одежда")
        self.cnopca3=cnopci.Cnopci(650,350,cartincacnop3,"Мини-игра")
        self.cnopca4=cnopci.Cnopci(650,450,cartincacnop4,"Улучшение")
        self.uvelith=ulytsh
        self.shrift=pygame.freetype.Font("Breeze Normal.Ttf",40)
        self.sobitieheath=pg.USEREVENT
        pg.time.set_timer(self.sobitieheath,random.randint(1000,10000))
        fayl=open("ceniulutsh","r")
        read=fayl.readlines()
        self.spisoculuts=[]
        for cen in read:
            d=int(cen)
            self.spisoculuts.append(d)
        self.sobitiegolod=pg.USEREVENT+1
        pg.time.set_timer(self.sobitiegolod,random.randint(1000,10000))
        self.sobitiehappy=pg.USEREVENT+2
        pg.time.set_timer(self.sobitiehappy,random.randint(1000,10000))
        self.menueda=menu.Menuedi(self)
        self.menuodejdi=menuodejdi.Menuodejdi(self)
        self.menuigri=menuigri.Miniigra(self)
        self.menu=None
        self.run()
    
    def run(self):
        while True:
            if self.menu==None:
                self.event()
                self.update()
                self.draw()
            else:
                self.menu.update()
                self.menu.draw()
                self.menu.event()
    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                file=open("haracteristica","w")
                file.write(str(self.money.hislo)+"\n")
                file.write(str(self.happy.hislo)+"\n")
                file.write(str(self.satiety.hislo)+"\n")
                file.write(str(self.health.hislo)+"\n")
                file.close()
                fayl=open("ylutsh","w")
                fayl.write(str(self.uvelith))
                fayl.close()
                fayl=open("cuplena","w",encoding="UTF-8")
                for odegda in self.menuodejdi.spisocodejdi:
                    fayl.write(odegda.cuplena+"\n")
                fayl.close()
                fayl=open("nadeta","w",encoding="UTF-8")
                for odegda in self.menuodejdi.spisocodejdi:
                    fayl.write(odegda.nadeta+"\n")
                fayl.close()
                fayl=open("ceniulutsh","w")
                for cena in self.spisoculuts:
                    fayl.write(str(cena)+"\n")
                fayl.close()
                pg.quit()
                exit()
            if event.type==pg.MOUSEBUTTONDOWN:
                if self.sostoanie=="igra":
                    if self.cobaka.pramougol.collidepoint(event.pos):
                        self.money.hislo=self.money.hislo+self.uvelith
                    if self.cnopca1.pramougol.collidepoint(event.pos):
                        self.menu=self.menueda
                        self.cnopca1.clic()
                    if self.cnopca2.pramougol.collidepoint(event.pos):
                        self.menu=self.menuodejdi
                        self.cnopca2.clic()
                    if self.cnopca3.pramougol.collidepoint(event.pos):
                        self.menu=self.menuigri
                        self.cnopca3.clic()
                    if self.cnopca4.pramougol.collidepoint(event.pos):
                        if len(self.spisoculuts)>0:
                            if self.money.hislo>self.spisoculuts[0]:
                                self.uvelith=self.uvelith+1
                                self.money.hislo=self.money.hislo-self.spisoculuts[0]
                                self.spisoculuts.pop(0)
                        self.cnopca4.clic()
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_6:
                    self.sostoanie="igra"
                    self.satiety.hislo=100
                    self.health.hislo=100
                    self.happy.hislo=100
                    for odejda in self.menuodejdi.spisocodejdi:
                        odejda.cuplena="Не куплена"
                        odejda.nadeta="Не надета"
                    self.spisoculuts=[140,240,340,440]
                    self.uvelith=1
                    self.money.hislo=0
            if event.type==self.sobitiegolod and self.sostoanie=="igra":
                self.satiety.hislo=self.satiety.hislo-random.randint(1,10)
            if event.type==self.sobitieheath and (self.satiety.hislo<30 or self.happy.hislo<30) and self.sostoanie=="igra":
                self.health.hislo=self.health.hislo-random.randint(1,10)
            if event.type==self.sobitiehappy and self.sostoanie=="igra":
                self.happy.hislo=self.happy.hislo-random.randint(1,10)
    def update(self):
        if self.health.hislo<0:
            self.sostoanie="menu"
    def draw(self):
        self.screen.blit(fon,[0,0])
        self.cobaka.otrisovca(self.screen)
        self.satiety.otrisovca(self.screen)
        self.money.otrisovca(self.screen)
        self.health.otrisovca(self.screen)
        self.happy.otrisovca(self.screen)
        self.cnopca1.otrisovca(self.screen)
        self.cnopca2.otrisovca(self.screen)
        self.cnopca3.otrisovca(self.screen)
        self.cnopca4.otrisovca(self.screen)
        if self.health.hislo<0:
                self.shrift.render_to(self.screen,[350,100],"Вы проиграли")
        for odejda in self.menuodejdi.spisocodejdi:
            if odejda.nadeta=="Надета":
                odejda.otrisovca(self.screen)
        if len(self.spisoculuts)>0:
            self.shrift.render_to(self.screen,[550,450],str(self.spisoculuts[0]))
        else:
            self.shrift.render_to(self.screen,[550,420],"Нету улучшений")
        pg.display.flip()
        



Game()

