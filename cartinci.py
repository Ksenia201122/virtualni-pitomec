import pygame as pg
from nastroici import *
import os

fon=pg.image.load("images/background.png")
fon=pg.transform.scale(fon,[SCREEN_WIDTH,SCREEN_HEIGHT])
happy=pg.image.load("images/happiness.png")
happy=pg.transform.scale(happy,[100,100])
health=pg.image.load("images/health.png")
health=pg.transform.scale(health,[100,100])
satiety=pg.image.load("images/satiety.png")
satiety=pg.transform.scale(satiety,[100,100])
money=pg.image.load("images/money.png")
money=pg.transform.scale(money,[100,100])
cartincacnop=pg.image.load("images/button.png")
cartincacnop=pg.transform.scale(cartincacnop,[200,65])
cartincacnop2=pg.image.load("images/button.png")
cartincacnop2=pg.transform.scale(cartincacnop2,[200,65])
cartincacnop3=pg.image.load("images/button.png")
cartincacnop3=pg.transform.scale(cartincacnop3,[200,65])
cartincacnop4=pg.image.load("images/button.png")
cartincacnop4=pg.transform.scale(cartincacnop4,[200,65])
najata=pg.image.load("images/button_clicked.png")
najata=pg.transform.scale(najata,[200,65])
menu=pg.image.load("images/menu/menu_page.png")
menu=pg.transform.scale(menu,[SCREEN_WIDTH,SCREEN_HEIGHT])
menuigri=pg.image.load("images/game_background.png")
menuigri=pg.transform.scale(menuigri,[SCREEN_WIDTH,SCREEN_HEIGHT])
nazvedi=os.listdir("images/food")
nazvodejdi=os.listdir("images/items")
nazvigrush=os.listdir("images/toys")
spisoccartedi=[]
spisoccarodejdi=[]
spisoccarigrush=[]
for nazvanieedi in nazvedi:
    cartinca=pg.image.load("images/food/"+nazvanieedi)
    cartinca=pg.transform.scale(cartinca,[200,200])
    spisoccartedi.append(cartinca)
for nazvanieodejdi in nazvodejdi:
    cartinca=pg.image.load("images/items/"+nazvanieodejdi)
    cartinca=pg.transform.scale(cartinca,[250,250])
    spisoccarodejdi.append(cartinca)
for nazvanieigrushci in nazvigrush:
    cartinca=pg.image.load("images/toys/"+nazvanieigrushci)
    cartinca=pg.transform.scale(cartinca,[100,100])
    spisoccarigrush.append(cartinca)





