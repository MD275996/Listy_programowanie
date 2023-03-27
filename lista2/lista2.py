import string
import math
from PIL import Image
import os, sys
from random import randint
from zipfile import ZipFile
from datetime import date
import PyPDF2 as pypdf

def passwd(n = 8, s=string.ascii_letters+string.digits+string.punctuation):
    haslo = ""
    for i in range(n):
        haslo += s[randint(0,len(s)-1)]
    return haslo


def mini(sciezka,w,h,nowa_nazwa):

    stare = Image.open(sciezka)
    nowe = stare.resize((w,h))
    nowe.save(nowa_nazwa+".jpg")
    #jak ma dzialac podawanie sciezki do pliku?
 
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

def split_pdf(sciezka,liczba_stron):
    mypdf = pypdf.PdfReader(sciezka)
    strona = 0
#pierwszy przypadek, pliki zawierające daną liczbę stron
    if type(liczba_stron) == int:
        ile = math.floor(len(mypdf.pages)/liczba_stron)
        ogonek = len(mypdf.pages)%liczba_stron
        
        for i in range(ile):
            nowypdf = pypdf.PdfWriter()
            for j in range(liczba_stron):
                nowypdf.add_page(mypdf.pages[strona])
                strona+=1
            with open("sample_cut_"+str(i)+".pdf","wb") as fp:
                nowypdf.write(fp)
        for k in range(ogonek):
            nowypdf.add_page(mypdf.pages[strona])
            strona+=1
        with open("sample_cut_"+str(ile+1)+".pdf","wb") as fp:
            nowypdf.write(fp)

#drugi przypadek, pliki zawieraja rozne ilosci stron podane w postaci 14-27 w tablicy
    elif type(liczba_stron) == list:
        for i in range(len(liczba_stron)):
            nowypdf = pypdf.PdfWriter()
            przedział = liczba_stron[i].split("-")
            
            for j in range(int(przedział[0])-1,int(przedział[1])):
                nowypdf.add_page(mypdf.pages[j])
            with open("sample_cut_"+str(i)+".pdf","wb") as fp:
                nowypdf.write(fp)  

def dodawanie(dzialanie):
    #dodawanie
    dane = dzialanie.split("+")
    wynik = 0
    for el in dane:
        wynik = wynik + int(el)
    
    for k in range(len(dane)):
        print(" "*(len(str(wynik))-len(dane[k]))+dane[k])
    
    print("+"+" "*(len(str(wynik))-1))
    print("-"*len(str(wynik)))
    print(wynik)  

safe_copy(["katalog1","katalog2","katalog3"])

