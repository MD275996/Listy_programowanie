#Kalkulator walut z dodatkowymi funkcjami napisany za pomocą TkInter

#strona z której korzystałem, by używać tkinter https://coderslegacy.com/python/python-gui/

from tkinter import *

root = Tk()             #Toplevel widget of Tk which represents mostly the main window of an          application. It has an associated Tcl interpreter.

root.geometry("200x150")
frame = Frame(root)     #Frame widget which may contain other widgets and can have a 3D border.
frame.pack()


root.title("Test")
root.mainloop()




# print(type(root))
# print(type(frame))