#program ma rysować graf w pętli, w każdym kroku doda kolejną wartość do dziedziny i wypisze(doklei) na wykres, ten zas ma byc zapisany jaki plik
#wymiary jak i rozmiar dziedziny będą ustalone

import matplotlib.pyplot as plt
import random as rand
import glob
import os
from PIL import Image

def bladzenie_agetna(kroki=25):
    #przygotowanie do petli
    tab_x=[1]
    tab_y=[0]
    poziom_y=0
    fig, axs = plt.subplots()
    axs.set(xlim=(0,kroki), ylim=(-1*kroki/2,kroki/2))
    axs.plot(tab_x,tab_y)
    plt.savefig("pliki\\fig0.png")

    for i in range(1,kroki):
        tab_x.append(i+1)
        if rand.randint(0,1) == 1:
            poziom_y +=2
            tab_y.append(poziom_y)
        else:
            poziom_y -= 2
            tab_y.append(poziom_y)
        axs.plot(tab_x,tab_y)
        plt.savefig("pliki\\fig"+str(i)+".png")
    
    #po zapisaniu plików do folderu zrobimy z nich gif za pomocą kodu ze strony
    #https://www.blog.pythonlibrary.org/2021/06/23/creating-an-animated-gif-with-python/

    tab_sorted=[]
    for i in range(len(glob.glob(f"pliki\\*.PNG"))):
        tab_sorted.append("pliki\\fig"+str(i)+".png")
    print(tab_sorted)

    frames = [Image.open(image) for image in tab_sorted]
    frame_one = frames[0]
    frame_one.save("chodzący_graf.gif", format="GIF", append_images = frames, save_all=True, duration=100, loop=0)



bladzenie_agetna(12)
    