#!/usr/env/bin python3

import sys
import numpy as np
import matplotlib.pyplot as plt

def seir_model(n0, s, e, i, r,beta, sigma, gamma):
    """
        Opis:  
            Funkcja symuluje przebieg epidemii według modelu SEIR i rysuje wykres przedstawiający zachowanie
            grup modelu w trakcie trwania epidemii

        Argumenty:
            n0 : int
                określa liczbę ludności, na której przeprowadzana jest symulacja
            
            s  : int
                określa liczbę zdrowych ludzi
            
            e  : int
                określa liczbę zarażonych ludzi
            
            i  : int
                określa liczbę zarażających
            
            r  : int
                określa liczbę ozdrowiałych  

            beta : float
                określa wskaźnik infekcji (jej tempo rozprzestrzeniania się)
            
            sigma : float
                określa czas inkubacji, czyli kiedy osoba z zarażonej stanie się zarażającą

            gamma : float
                określa wskaźnik ozdrowień

            
                
        Zwraca:
            Wypisuje wykres przedstawiający przebieg symulacji epidemii      
        
        """    

#zdeklarowanie tablic w których będą przechowywane wartości, gdzie index oznacza daną jednostę czasu, do wykresów
    tablica_S=[s]
    tablica_E=[e]
    tablica_I=[i]
    tablica_R=[r]

    time = 150 #dni
    for t in range(time):
        tS = s + -1*(beta*s*i)/n0
        tE = e + (beta*s*i)/n0 - sigma*e
        tI = i + sigma*e - gamma*i
        tR = r + gamma*i

        tablica_S.append(tS)
        tablica_E.append(tE)
        tablica_I.append(tI)
        tablica_R.append(tR)
        s, e, i, r = tS, tE, tI, tR


    x = np.array(range(0,time+1))
    
    """plot = plt.figure(figsize=(5,2.7), layout="constrained")
    plt.plot(x,tablica_S, label="Susceptible")
    plt.plot(x,tablica_E, label="Exposed")
    plt.plot(x,tablica_I, label="Infectious")
    plt.plot(x,tablica_R, label="Recovered")
    plt.xlabel("Czas (dni)")
    plt.ylabel("Procent")
    plt.title("SEIR Model")
    plt.legend()
    plt.show()
    """
    


if __name__ == "__main__":
    tab_arg = list(sys.argv) #bardzo ważne!!!
    tab_arg.remove(tab_arg[0])
    #print(tab_arg)
    for i in range(len(tab_arg)):
        tab_arg[i] = float(tab_arg[i])
    #print(tab_arg)

    #n0, s, e, i, r, beta, sigma, gamma = tab_arg #wartości początkowe
    #seir_model(n0,s,e,i,r,beta,sigma,gamma)
    
    r = seir_model(1000,999,1,0,0, 1.34,0.19,0.34)
    r.savefig("standard.png")
    seir_model(1000,999,1,0,0, 0.75,0.19,0.34).savefig("beta_0.75_.png")
    seir_model(1000,999,1,0,0, 1.34,0.10,0.34).savefig("sigma_0.10_.png")
    seir_model(1000,999,1,0,0, 1.34,0.19,0.08).savefig("gamma_0.28_.png")
    