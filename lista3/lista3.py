import requests
from bs4 import BeautifulSoup
import PyPDF2 as pypdf
import webbrowser
from datetime import date
import os
from zipfile import ZipFile
import qrcode
import cv2
import aspose.words as aw


def zad1(rozszrz, katalogi, liczba_dni = 3):
    """
    Opis:  
        Funkcja tworząca kopię zapasową plików o zadanym rozszerzeniu i ostatniej dacie modyfikacji 
        z zadanego folderu (folderów) w nowo utworzonym katalogu 'Backup'

    Argumenty:
        rozszrz : str 
            określa rozszerzenie, według którego będą dobrane pliku do skopiowania
                
        katalogi : str, list
            określa katalog lub liste katalogów z których mają być wyszukane pliki do skopiowania

        liczba_dni: int
            kryterium przy wyszukiwaniu, określa jak stare będą pliki brane do skopiowania (domyślnie = 3)

    Zwraca:
        nowo utworzony katalog z kopią bezpieczeństwa zapisany w katalogu programu
    
    """    
    
    dzisiaj = date.today()
    os.mkdir("Backup")
    with ZipFile("Backup\\copy-" + str(dzisiaj) + ".zip","w") as myzip:
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
def zad2(plik):                                  
    file = open(plik,'r')
    file2 = open("nowy.txt",'w')
    print(repr(file.read()))
    raw_text = repr(file.read())



    # if '\n' in raw_text:
    #     print("A")
    #     splitted = raw_text.split('\n')
    #     new_text = str.join("",splitted)
    #     file2.write(new_text)
    #     print(new_text)
    #     file2.close()
    # else:
    #     print("B")
    #     splitted = raw_text.split('\r')
    #     new_text = str.join('\r\n',splitted)
    #     file2.write(new_text)
    #     print(new_text)
    #     file2.close()

def compare_pdf(nowy_pdf, stary_pdf):
    """
    Opis:  
        Funkcja pomocnicza, sprawdza czy dwa pdf są identyczne.
        Działa dla prostych pdf-ów, źródło kodu: https://blog.aspose.com/pl/words/compare-pdf-files-in-python/

    Argumenty:
        nowy_pdf : str
            ścieżka do pierwszego pliku pdf
        stary_pdf : str
            ścieżka do drugiego pliku pdf
                
    Zwraca:
        Wypisuje na ekran odpowiedź czy dwa pliki pdf są identyczne
    
    """

    #załadowanie plików pdf
    pdf1 = aw.Document(nowy_pdf)
    pdf2 = aw.Document(stary_pdf)

    #konwertuje na dokument WORD
    pdf1.save("nowy.docx", aw.SaveFormat.DOCX)
    pdf2.save("stary.docx", aw.SaveFormat.DOCX)

    doc1 = aw.Document("nowy.docx")
    doc2 = aw.Document("stary.docx")

    #ustalenie opcji porównania
    options = aw.comparing.CompareOptions()            
    options.ignore_formatting = True
    options.ignore_headers_and_footers = True
    options.ignore_case_changes = True
    options.ignore_tables = True
    options.ignore_fields = True
    options.ignore_comments = True
    options.ignore_textboxes = True
    options.ignore_footnotes = True

    doc1.compare(doc2, "user", date.today(), options)

    if(doc1.revisions.count == 0):
        print("pliki są identyczne")
    else:
        print("pliki nie są te same")

    os.remove("nowy.docx")
    os.remove("stary.docx")


def zad3(lista_pdf):
    """
    Opis:  
        Funkcja łącząca kilka plików pdf w jeden

    Argumenty:
        lista_pdf : list 
            lista ścieżek do plików pdf, które mają być złączone w jeden
                
    Zwraca:
        plik pdf powstały z zadanych, zapisany jako 'sklejka.pdf' w folderze programu,
        dodatkowo informuje czy operacja się udałą
    
    """
    nowypdf = pypdf.PdfWriter()
    for el in lista_pdf:
        obecny_pdf = pypdf.PdfReader(el)
        for i in range(len(obecny_pdf.pages)):
            nowypdf.add_page(obecny_pdf.pages[i])
    nowypdf.write("sklejka.pdf")

    #sprawdzenie czy operacja się powiodła
    compare_pdf("sklejka.pdf","sample.pdf")
    
    
    


def zad4(dane):
    """
    Opis:   
        Funkcja tworząca kod QR lub czytająca go.     
        Jeśli podana będzie ścieżka do zdjęcia .png lub .jpg to wykryje kod QR i odczyta wiadomość, w przeciwnym razie zakoduje podany string

    Argumenty:
        dane : str 
            - wiadomość do zakodowania
            - ścieżka do zdjęcia kodu QR, który ma być odczytany
                
    Zwraca:
        Plik png z kodem QR zapisany w folderze programu, lub wiadomość zakodowaną pod kodem QR
    
    """
    
    if ".png" in dane or ".jpg" in dane:
        try:
            img = cv2.imread(dane)
            detect = cv2.QRCodeDetector()
            value, points, straight_qrcode = detect.detectAndDecode(img)
            print(value)
        except:
            return 
    else:
        img = qrcode.make(dane)
        img.save("kodqr.png")
    #bibliografia https://www.google.com/search?q=python+read+qr+code&client=firefox-b-d&ei=_7U2ZM9Uj7SuBIHAhcAC&ved=0ahUKEwiP0KmUvaT-AhUPmosKHQFgASgQ4dUDCA8&uact=5&oq=python+read+qr+code&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBQgAEIAEMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoKCAAQRxDWBBCwAzoKCAAQigUQsAMQQzoICAAQgAQQsQM6CwgAEIAEELEDEIMBSgQIQRgAULYHWLQXYOEZaAFwAXgAgAFbiAHcB5IBAjEymAEAoAEByAEKwAEB&sclient=gws-wiz-serp

    

def zad5(tekst):
    """
    Opis:   
        Funkcja sprawdzające czy w podanym ciągu znaków zostały poprawnie użyte nawiasy tzn. jest ich odpowiednia ilość, są poprawnie zagnieżdżone, są odróżnione

    Argumenty:
        tekst : str 
            Tekst którego zapis nawiasów ma zostać sprawdzony
                

    Zwraca:
        Odpowiedź czy nawiasy są poprawnie zapisane
    
    """
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
                


def zad6():
    """
    Opis: 
        Program proponujący użytkownikowi tytuły artykułów z Wikipedii, pytająca czy wyświetlić dany artykuł i wyświetlająca w przypadku pozytywnej odpowiedzi

    Argumenty:
        brak

    Zwraca:
        Proponuje tutył artukułu z Wikipedii i otwiera go
    
    """
    
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
    
    


zad3(["sample_cut_0.pdf","sample_cut_1.pdf","sample_cut_2.pdf","sample_cut_3.pdf"])
#zad5("()()([])")
#zad6()