#Kalkulator walut z dodatkowymi funkcjami napisany za pomocą TkInter

#strona z której korzystałem, by używać tkinter https://coderslegacy.com/python/python-gui/

#TO-DO:
# -rozmieścić elementy w oknie
# -stworzyć funkcję pobierającą dane ze strony NBP
# -stworzyć i przypisać funkcje do przycisków

#program będzie korzystał z kalkulacji walut przez google, jednak będzie trzeba tylko pobrać baze danych walut,
#potem tylko będziemy wysyłać zapytanie do googla [ilość] [waluta] to [waluta] i za pomocą beautyful soup pobierać wynik


from tkinter import *
import tkinter.ttk as ttk
import requests
import json

# ============================ pobranie danych  =======================================
my_dict = {}                                            #tutaj chcemy by trafiły nasze dane
r = requests.get("http://api.nbp.pl/api/exchangerates/tables/a/")

if r.status_code == 200:
    data = json.loads(r.text)
    waluty = data[0]['rates']                           #pod rates są słowniki z każdą nazwą waluty i jej kursem

    for i in range(len(waluty)):
        my_dict["[" + waluty[i]["code"]+"] " + waluty[i]["currency"]] = waluty[i]["mid"]
    my_dict["[PLN] złoty polski"] = 1
    json_object = json.dumps(my_dict, indent=1)
    with open("kursy_offline.json","w") as file:
        file.write(json_object)
        file.close()
else:
    with open("kursy_offline.json","r") as file:        #pobiera dane z pliku gdy nie ma połączenia z internetem
        my_dict = json.loads(file.read())
#======================================================================================


#=============================== deklaracja funkcji ===================================

def przelicz(curr_in,curr_out,value):
    #przeliczenie na złotówki
    pln = my_dict[curr_in]*value
    #przeliczenie na walute docelową
    out = round(pln/my_dict[curr_out],2)

    return out

def zmiana_clicked():
    buffor = combo_opcja2.get()
    combo_opcja2.set(combo_opcja1.get())
    combo_opcja1.set(buffor)

def oblicz_clicked():
    curr_in = combo_opcja1.get()
    curr_out = combo_opcja2.get()
    value = float(entry_waluta.get())
    print(curr_in,curr_out,value)
    output = przelicz(curr_in, curr_out, value)
    wynik.set(output)

#======================================================================================


#============================= RYSOWANIE OKNA =========================================

root = Tk()             #Toplevel widget of Tk which represents mostly the main window of an application. It has an associated Tcl interpreter.

root.geometry("700x200")                        #wymiaru okna programu

frame = Frame(root)      #stwarzamy "pojemnik" za pomocą Frame, który będzie umiejscowiony na górze    
frame.pack()

left_frame = Frame(root)   #pojemnik umiejscowiony na lewo
left_frame.pack(side=LEFT)

right_frame = Frame(root)#pojemnik umiejscowiony na prawo
right_frame.pack(side=RIGHT)

#======================================================================================


#============================= Frame, góra ============================================

waluty= list(my_dict.keys())        #przygotowujemy do droplistów


combo_opcja2 = ttk.Combobox(frame, values=waluty,width=len(max(waluty)),)       #stwarzamy combobox i wsadzamy go jako pierwszego, czyli będzie na prawo
combo_opcja2.set(waluty[1])
combo_opcja2.pack(side=RIGHT,padx=10,pady=10)


button_zamiana = Button(frame, text="zamiana", command=zmiana_clicked)      #stwarzamy button, przypisujemy funkcję i wsadzamy
button_zamiana.pack(side=RIGHT,padx=10,pady=10)


combo_opcja1 = ttk.Combobox(frame, values=waluty,width=len(max(waluty)))       #stwarzamy combobox, pierwszy od lewej
combo_opcja1.set(waluty[0])
combo_opcja1.pack(padx=10,pady=10)

#======================================================================================


#=================================== Left =============================================

entry_waluta = Entry(left_frame)
entry_waluta.pack(padx=30,pady=20)

button_oblicz = Button(left_frame,text="oblicz", command=oblicz_clicked)
button_oblicz.pack()

#======================================================================================


#================================== Right =============================================

wynik = StringVar()
wynik.set("Tutaj wyświetli się wynik")

label_wynik = Label(right_frame, textvariable=wynik)
label_wynik.pack(padx=30,pady=20)


button_zakoncz = Button(right_frame, text="zakończ")
button_zakoncz.pack()

#======================================================================================

root.title("Kalkulator walut")
root.mainloop()



#NOTATKI Z LEKCJI
#korzystać z tkinter
#dane o kursach pobierać z api.nbp.pl za pomocą request.get
#zapisać ostatnią uzyskaną tabelę z internetu, w przypadku jakby nie było połączenia
