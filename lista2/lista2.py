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
             
def water_mark():
    znak_wodny = Image.open("waterMark.png")
    znak_wodny = znak_wodny.convert("RGBA")
    znak_wodny.putalpha(127)    
    znak_wodny.save("alpha.png")

def slupek(dzialanie):


    #robimy słupek pojedyńczego działania (dodawania lub mnozenia)

    if "+" in dzialanie:

        dane = dzialanie.split("+")     #dodawanie (i odejmowanie) są ostatnimi działaniami jakie podejmujemy, więc jeśli po rozbiciu, elementy tablicy będą zawierały znaki mnożenia, nimi zajmiemy się najpierw
        
        wynik = 0
        for el in dane:
            wynik = wynik + int(el)     #obliczamy wynik, by poznać jak szeroki ma być słupek
        
        for k in range(len(dane)):      #w tej pętli rozpisujemy słupek, odpowiednio sformatowany
            print(" "*(len(str(wynik))-len(str(dane[k])))+str(dane[k])) 

                                        #zakończenie słupka, podkreślenie i wynik
        print("+"+" "*(len(str(wynik))-1))
        print("-"*len(str(wynik)))
        print(wynik)
    elif "*" in dzialanie:
        dane = dzialanie.split("*")

        wynik = int(dane[0])*int(dane[1])

        spacja_lewo = len(str(wynik))
        spacja_prawo = 0

        #zaczynamy pisac slupek mnozenia
        print(" "*(spacja_lewo-len(dane[0]))+dane[0])
        print(" "*(spacja_lewo-len(dane[1]))+dane[1])
        print("*"+" "*(spacja_lewo-1))
        print("="*spacja_lewo)
        #piszemy kazde mnozenie osobno
        for i in range(len(dane[0])):
            print(" "*(spacja_lewo-len(str(int(dane[0][-i+1])*int(dane[1])))-spacja_prawo) + str(int(dane[0][-(i+1)])*int(dane[1])) + " "*spacja_prawo)
            spacja_prawo+=1
        print("+" + " "*spacja_lewo)    
        print("="*spacja_lewo)
        print(wynik)
        return(wynik)
                                    #po pomnożeniu dostajemy nową tablicę, i na niej wykonujemy mnożenie

# def mnozenie(dzialanie):
#     if(len(dane)>2):
#         dane[0] = mnozenie(dane.pop(1)+"*"+dane[0])
#     else:


slupek("12*15")
