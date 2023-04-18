#!/usr/env/bin python3

import sys
import numpy as np
import matplotlib.pyplot as plt

def seir_model(n0, s, e, i, r,beta, sigma, gamma):

#zdeklarowanie tablic w których będą przechowywane wartości, gdzie index oznacza daną jednostę czasu, do wykresów
    tablica_S=[s]
    tablica_E=[e]
    tablica_I=[i]
    tablica_R=[r]

    time = 500 #dni
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

    #mamy teraz dane, warto je przemienić na procenty, a potem wsadzić w wykres


    x = np.array(range(0,501))
    plt.figure(figsize=(5,2.7), layout="constrained")
    plt.plot(x,tablica_S, label="Susceptible")
    plt.plot(x,tablica_E, label="Exposed")
    plt.plot(x,tablica_I, label="Infectious")
    plt.plot(x,tablica_R, label="Recovered")
    plt.xlabel("Czas (dni)")
    plt.ylabel("Procent")
    plt.title("SEIR Model")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    tab_arg = list(sys.argv) #bardzo ważne!!!
    tab_arg.remove(tab_arg[0])
    print(tab_arg)
    for i in range(len(tab_arg)):
        tab_arg[i] = float(tab_arg[i])
    print(tab_arg)

    n0, s, e, i, r, beta, sigma, gamma = tab_arg #wartości początkowe
    seir_model(n0, s, e, i, r, beta, sigma, gamma)







