import PyPDF2 as pypdf

#liczba dni jest do ustalenia, dla sprawdzenia w folderze jeden plik nie spełnia wymagań, ma wykonać kopie wszystkich podfolderów
def zad1(rozszrz, katalogi, liczba_dni = 3):
    return 0

#Przeczytać o CRTL, w windowsie: \r \n, a w unixie jest tylko \r, zalecane użycie Notepad++ -> Edycja -> zmiana znaku końca linii
def zad2():                                  
    return 0

#Działanie odwrotne do zadania z listy 2, użyć by sprawdzić działanie, porównać pliki
def zad3(lista_pdf):
    nowypdf = pypdf.PdfWriter()
    for el in lista_pdf:
        obecny_pdf = pypdf.PdfFileReader(el)
        for i in range(len(obecny_pdf.pages)):
            nowypdf.add_page(obecny_pdf.pages[i])
    nowypdf.write("sklejka.pdf")
    



#zmienić wiadomość, zwykły string na kod QR, zakodować i odkodować
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
                


# nie działa w nieskończoność, ma 5 prób,
def zad6():
    return 0

zad3(["sample_cut_0.pdf","sample_cut_1.pdf","sample_cut_2.pdf","sample_cut_3.pdf","sample_cut_4.pdf","sample_cut_5.pdf","sample_cut_6.pdf","sample_cut_7.pdf"])