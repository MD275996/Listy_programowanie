#Kalkulator walut z dodatkowymi funkcjami napisany za pomocą TkInter

#strona z której korzystałem, by używać tkinter https://coderslegacy.com/python/python-gui/

#TO-DO:
# -rozmieścić elementy w oknie
# -stworzyć funkcję pobierającą dane ze strony NBP
# -stworzyć i przypisać funkcje do przycisków

from tkinter import *

root = Tk()             #Toplevel widget of Tk which represents mostly the main window of an          application. It has an associated Tcl interpreter.

root.geometry("800x450")
frame = Frame(root, width=800 ,height=100)     #Frame widget which may contain other widgets and can have a 3D border.
frame.pack(padx=20,pady=20)

left_frame = Frame(root,width=400,height=350)
left_frame.pack(side=LEFT)

right_frame = Frame(root, width=400, height=350)
right_frame.pack(side=RIGHT)

#ustawiliśmy główne części okna, w które będziemy wsadzać elementy, czyli góra, lewo i prawo
#dodamy elementy do pierwszego okna

waluty=["PLN", "EUR"]           #dane do pobrania ze strony NBP
waluta1 = StringVar(value = waluty[0])
waluta2 = StringVar(value = waluty[1])

#pierwszy droplist
optionmenu_opcja1 = OptionMenu(frame, waluta1, *waluty) #gwiazdka rozpakowywuje dane z tablicy
optionmenu_opcja1.pack(expand=TRUE, fill= BOTH, side=RIGHT,  padx= 50)

#button zmieniający
button_zamiana = Button(frame, text="zamiana")
button_zamiana.pack(side=RIGHT, padx=50)

#drugi droplist
optionmenu_opcja2 = OptionMenu(frame, waluta2, *waluty)
optionmenu_opcja2.pack(expand=TRUE, fill= BOTH, padx= 50)

#lewa strona

entry_waluta = Entry(left_frame)
entry_waluta.pack()

button_oblicz = Button(left_frame,text="oblicz")
button_oblicz.pack()

#prawa strona

wynik = StringVar()
wynik.set("Tutaj wyświetli się wynik")

label_wynik = Label(right_frame, textvariable=wynik)
label_wynik.pack()


button_zakoncz = Button(right_frame, text="zakończ")
button_zakoncz.pack()

root.title("Kalkulator walut")
root.mainloop()




# print(type(root))
# print(type(frame))