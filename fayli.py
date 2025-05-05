# fayl=open("eda.py","r")
# print(fayl)
# read=fayl.read()
# print(read)
# fayl.close()
# fayl=open("wsr.tecst","w")
# fayl.write("abc\n")
# fayl.write("def\n")
# fayl.close()
# fayl=open("wsr.tecst",'a',encoding="UTF-8")
# fayl.write("фкн")
# fayl.close()

# r=0
# while r==0:
#     print("1.название файла и его содержимое,2.Создать файл и записать в него текст,3.Добавить текст в файл,4.выйти")
#     vibor=int(input("Какой пункт хотите выбрать?"))
#     if vibor==1:
#         profayl=input("Какое название файла?")
#         fayl=open(profayl,"r")
#         read=fayl.read()
#         print(read)
#         fayl.close()
#     if vibor==2:
#         ob=input("Какой файл?")
#         oz=input("Какой текст записать в файл?")
#         fayl=open(ob,"w")
#         fayl.write(oz+"\n")
#         fayl.close()
#     if vibor==3:
#         ad=input("Какой файл?")
#         ap=input("Какой текст записать в файл?")
#         fayl=open(ad,"a")
#         fayl.write(ap+"\n")
#         fayl.close()
#     if vibor==4:
#         r=1

# def v(sushfayl,nesushfayl):
#     fayl1=open(sushfayl,"r")
#     fayl2=open(nesushfayl,"w")
#     read=fayl1.read()
#     fayl2.write(read)
#     fayl2.close()
#     fayl1.close()
# v("er","fer")

# def d(spisoc,nazvfayl):
#     fayl=open(nazvfayl,"w",encoding="UTF-8")
#     for otdelgorod in spisoc:
#         fayl.write(otdelgorod+"\n")
#     fayl.close()
# d(["Москва","Новгород","Воронеж"],"goroda")

# def j(fayl,simvol):
#     file=open(fayl,"r")
#     read=file.read()
#     v=0
#     for h in read:
#         if h==simvol:
#             v=v+1
#     return v
# a=j("cobaka.py","a")
# print(a)

r=0
# while r==0:
#     f=""
#     om=input("Какое имя?")
#     if om=="":
#         r=1
#     else:
#         fayl=open("goroda","a") 
#         fayl.write(om+"\n")
#         fayl.close()

# fayl=open("shisla","r")
# read=fayl.readlines()
# spisoc=[]
# for sr in read:
#     a=int(sr)
#     spisoc.append(a)
# fayl.close()
# fayl=open("shisla","w")
# spisoc.sort()
# for cv in spisoc:
#     fayl.write(str(cv)+"\n")
# fayl.close()

# def stro(simvol,fayl):
#     fayl=open(fayl,"r")
#     read=fayl.readlines()
#     a=0
#     for tr in read:
#         if simvol in tr:
#             a=a+1
#     fayl.close()
#     return a
# z=stro("e","odejda.py")
# print(z)

# def er(tecst,file,shislostr):
#     fayl=open(file,"r")
#     read=fayl.readlines()
#     spisocdostr=read[0:shislostr-1]
#     spisocpostr=read[shislostr-1:]
#     fayl.close()
#     fayl=open(file,"w")
#     for f in spisocdostr:
#         fayl.write(f)
#     fayl.write(tecst+"\n")
#     for y in spisocpostr:
#         fayl.write(y)
#     fayl.close()
# er("hhhh","igrushci.py",8)

# def fa(fayl,shislo1,shislo2):
#     shislo1=shislo1-1
#     shislo2=shislo2-1
#     file=open(fayl,"r")
#     read=file.readlines()
#     spisocdopervoy=read[0:shislo1]
#     odnastr=read[shislo1]
#     str=read[shislo1+1:shislo2]
#     vtorasrt=read[shislo2]
#     spisocposle=read[shislo2+1:]
#     file.close()
#     file=open(fayl,"w")
#     for v in spisocdopervoy:
#         file.write(v)
#     file.write(vtorasrt)
#     for t in str:
#         file.write(t)
#     file.write(odnastr)
#     for b in spisocposle:
#         file.write(b)
#     file.close() 
# fa("igrushci.py",3,5)

def la(fayl,shislostr):
    shislostr=shislostr-1
    file=open(fayl,"r")
    read=file.readlines()
    spisocdostr=read[0:shislostr]
    str=read[shislostr]
    spisocposlestr=read[shislostr+1:] 
    file.close()
    file=open(fayl,"w")
    for t in spisocposlestr:
        file.write(t)
    file.write(str)
    for g in spisocdostr:
        file.write(g)
    file.close()
la("s",4) 
    





