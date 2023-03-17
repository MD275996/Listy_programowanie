import string
from PIL import Image
import os, sys
from random import randint
from zipfile import ZipFile
from datetime import date

# def passwd(n = 8, s=string.ascii_letters+string.digits+string.punctuation):
#     haslo = ""
#     for i in range(n):
#         haslo += s[randint(0,len(s)-1)]
#     return haslo


def mini(sciezka,w,h,nowa_nazwa):

    stare = Image.open(sciezka)
    nowe = stare.resize((w,h))
    nowe.save(nowa_nazwa+".jpg")
    #jak ma działać podawanie ścieżki do pliku?
 
def safe_copy(dane):
    dzisiaj = date.today()
    if type(dane) == str:
        katalog = dane.split("\\")[-1]
        with ZipFile(str(dzisiaj)+"_"+katalog+".zip","w") as myzip:
            myzip.write(dane)
            myzip.close()
    
    
    elif type(dane) == list:
        for el in dane:
            katalog = el.split("\\")[-1]
            with ZipFile(str(dzisiaj)+"_"+katalog+".zip","w") as myzip:
                myzip.write(el)
                myzip.close()

    

safe_copy(["katalog1","katalog2","katalog3"])

