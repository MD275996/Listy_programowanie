import requests
from bs4 import BeautifulSoup
import PyPDF2 as pypdf
import webbrowser
from datetime import date
import os
from zipfile import ZipFile

#gotowe
def zad1(rozszrz, katalogi, liczba_dni = 3):
    
    dzisiaj = date.today()
    with ZipFile("copy-" + str(dzisiaj) + ".zip","w") as myzip:
        if type(katalogi) == str:
                for folder, podfolder, pliki in os.walk(katalogi):
                    for nazwa_pliku in pliki:
                        plik_sciezka = os.path.join(folder, nazwa_pliku)
                        info = os.stat(plik_sciezka)                                                    #pobranie informacji o pliku
                        roznica_dni = dzisiaj - date.fromtimestamp(info.st_mtime)                       #obliczenie minionego czasu od ostatniej modyfikacji
                        if roznica_dni.days <= liczba_dni and nazwa_pliku.split(".")[-1] == rozszrz:    #sprawdzenie warunków
                            myzip.write(plik_sciezka)        
    
        elif type(katalogi) == list:
            for el in katalogi:
                for folder, podfolder, pliki in os.walk(el):
                    for nazwa_pliku in pliki:
                        plik_sciezka = os.path.join(folder, nazwa_pliku)
                        info = os.stat(plik_sciezka)
                        roznica_dni = dzisiaj - date.fromtimestamp(info.st_mtime)
                        if roznica_dni.days <= liczba_dni and nazwa_pliku.split(".")[-1] == rozszrz:
                            myzip.write(plik_sciezka)
                    
        myzip.close()


#Przeczytać o CRTL, w windowsie: \r \n, a w unixie jest tylko \r, zalecane użycie Notepad++ -> Edycja -> zmiana znaku końca linii
def zad2():                                  
    file = open("linie.txt")
    file.read()

#W połowie gotowe
def zad3(lista_pdf):
    nowypdf = pypdf.PdfWriter()
    for el in lista_pdf:
        obecny_pdf = pypdf.PdfReader(el)
        for i in range(len(obecny_pdf.pages)):
            nowypdf.add_page(obecny_pdf.pages[i])
    nowypdf.write("sklejka.pdf")
    
    #TO DO: sprawdzenie czy to są te same pliki
    



#zmienić wiadomość, zwykły string na kod QR, zakodować i odkodować
#dziwna dokumentacja
def zad4():
    return 0


#gotowe
def zad5(tekst):
    prawda = {"(":")", "[":"]", "{":"}", "<":">"}
    poprawne = True
    stos = []

    for el in tekst:
        if el in ["(","{","[","<"]:
            if len(stos)>0 and stos[-1] == el:
                poprawne = False
                break
            stos.append(el)
            
        elif el in [")","]","}",">"]:
            znak = stos.pop()
            if prawda[znak] != el:
                poprawne = False

    if poprawne:
        print("Wszystko ok!")
    else:
        print("Źle zapisane nawiasy")
                


# gotowe
def zad6():
    
    for i in range(5):

        request = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        
        if request.status_code == 200:    

            soup = BeautifulSoup(request.text,'html.parser')
            title_heading_tag = soup.find(id = "firstHeading")
            title_text = title_heading_tag.span.text

            pytanie = input("Czy wyświetlić artykuł o: " + title_text +"? (Y/N)")
            if pytanie == 'Y' or pytanie == 'y':
            
                #utworzenie odnośnika do danego artykułu
                link = "https://en.wikipedia.org/wiki/"
                parts = title_text.split(" ")
                ending = str.join("_",parts)
                link = link + ending

                webbrowser.open(link)
                pytanie2 = input("Czy chciałbyś zobaczyć inny artykuł? (Y/N)")
                if pytanie2=='Y' or pytanie2 =='y':
                    continue
                else:
                    break
            else:
                continue
        else:
            print("błąd połącznia")

    print("Enough internet for today. Go touch grass")
    
    

zad1("txt","folder",3)