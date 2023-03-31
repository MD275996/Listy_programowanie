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
             
def water_mark(zdjecie):
    znak_wodny = Image.open("waterMark.png")
    obraz = Image.open(zdjecie)
    obraz = obraz.convert("RGBA")
    #znak_wodny = znak_wodny.convert("RGBA")
    znak_wodny.putalpha(70)
    znak_wodny.save("znak_wodny.png")
    znak_wodny = znak_wodny.resize((50,50)) 
    
    nowyobraz = Image.new("RGBA",obraz.size,)
    nowyobraz.paste(obraz)
    nowyobraz.paste(znak_wodny,(round(nowyobraz.size[0]/2),round(nowyobraz.size[1]/2)))
    nowyobraz.save("zaznaczony.png")

def slupek(dzialanie):



    if "+" in dzialanie or "-" in dzialanie:
                                        #przyjmujemy że nie piszemy '-102+77'

        dane = dzialanie.split("+")     #rozdzielamy elementy po +, zostaną elementy takie jak '217-53'
        minusy = []
        for i in range(len(dane)):      #w tej pętli szukamy elementów przed którymi stoi minus i wyciągamy je, wsadzamy do osobnej tablicy i dodajemy na koniec pierwotnej tablicy
            if "-" in dane[i]:
                temp = dane[i]
                temp = temp.split("-") 
                dane[i] = temp[0]
                for j in range(1,len(temp)):
                    minusy.append("-" + temp[j])
        for al in minusy:
            dane.append(al)
        
        wynik = eval(dzialanie)    #obliczamy wynik, by poznać jak szeroki ma być słupek
        
        for k in range(len(dane)):      #w tej pętli rozpisujemy słupek, odpowiednio sformatowany
            print(" "*(len(str(wynik))-len(str(dane[k])))+str(dane[k])) 

                                        #zakończenie słupka, podkreślenie i wynik
        print("+"+" "*(len(str(wynik))-1))
        print("-"*len(str(wynik)))
        print(wynik)
    elif "*" in dzialanie:
        dane = dzialanie.split("*")

        wynik = int(dane[0])*int(dane[1])

        spacja_lewo = len(str(wynik)) # ustawiamy 'marginesy' dla ładnego wypisania słupka
        spacja_prawo = 0

        #zaczynamy pisac slupek mnozenia
        print(" "*(spacja_lewo-len(dane[0]))+dane[0])
        print(" "*(spacja_lewo-len(dane[1]))+dane[1])
        print("*"+" "*(spacja_lewo-1))
        print("="*spacja_lewo)
        #piszemy kazde mnozenie osobno
        for i in range(1,len(dane[0])+1):
            print(" "*(spacja_lewo-len(str(int(dane[0][-i])*int(dane[1])))-spacja_prawo) + str(int(dane[0][-(i)])*int(dane[1])) + " "*spacja_prawo)
            spacja_prawo+=1
        print("+" + " "*spacja_lewo)    
        print("="*spacja_lewo)
        print(wynik)
        return(wynik)
                                    #po pomnożeniu dostajemy nową tablicę, i na niej wykonujemy mnożenie



water_mark("images.jpg")
