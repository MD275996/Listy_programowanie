from random import randint as rand
import math

class Vector:
    def __str__(self):
        """
        Funkcja specjalna str
        
        Parametry: brak
        
        Output:
        
        """
        return(str(self.vector))
    
    def __init__(self,arg=3):
        """
        Funkcja specialna init
        
        Parametry: arg (domyślnie 3)
        
        Output: stwarza tablicę reprezentującą wektor o wielkości arg"""
        self.vector = []
        for i in range(0,arg):
            self.vector.append(0)
            
    def __getitem__(self,i):
        """
        Funkcja specialna getitem
        
        Parametry: i
        
        Output: zwraca za pomocą selektora [] element z tablicy self.vector na miejscu i"""
        return(self.vector[i])
        
    def __setitem__(self,i,x):
        """
        Funkcja specialna setitem
        
        Parametry: i , x
        
        Output: ustawia za pomocą selektora [] element w tablicy self.vector na miejscu i jako x"""
        self.vector[i] = x
        
    def __contains__(self,x):
        """
        Funkcja specialna contains
        
        Parametry: x
        
        Output: sprawdza czy w tablicy self.vector znajduje się element x"""
        b = False
        for i in range(0,len(self.vector)):
            if self.vector[i] == x:
                b = True
        return b        
    def __add__(self, vector2):
        """
        Funkcja specialna add
        
        Parametry: vector2 - w formie listy, krotki lub z klasy Vector
        
        Output: używa znaku '+' by odpowiednio dodać listy reprezentujące vectory"""
        if type(vector2) == Vector:
            if len(self.vector) == len(vector2.vector):
                output = []
                for i in range(0,len(self.vector)):
                   output.append(self.vector[i] + vector2.vector[i])
                self.vector = output
                return(output)
            else:
                raise ValueError("Różne wymiary!")
        else:
            if len(self.vector) == len(vector2):
                output = []
                for i in range(0,len(self.vector)):
                   output.append(self.vector[i] + vector2[i])
                self.vector = output
                return(output)
            else:
                raise ValueError("Różne wymiary!")
            
    def __sub__(self, vector2):
        """
        Funkcja specialna sub
        
        Parametry: vector2 - w formie listy, krotki lub z klasy Vector
        
        Output: używa znaku '-' by odpowiednio odjąć listy reprezentujące vectory"""
        if type(vector2) == Vector:
            if len(self.vector) == len(vector2.vector):
                output = []
                for i in range(0,len(self.vector)):
                   output.append(self.vector[i] - vector2.vector[i])
                self.vector = output
                return(output)
            else:
                raise ValueError("Różne wymiary!")
        else:
            if len(self.vector) == len(vector2):
                output = []
                for i in range(0,len(self.vector)):
                   output.append(self.vector[i] - vector2[i])
                self.vector = output
                return(output)
            else:
                raise ValueError("Różne wymiary!")
    def __mul__(self, a):
        """
        Funkcja specialna mul
        
        Parametry: a 
        
        Output: używa znaku '*' by odpowiednio pomnożyć wszystkie elementy listy self.vector przez skalar 'a' """
        try:
            a = float(a)
            output = []
            for i in range(0, len(self.vector)):
                output.append(self.vector[i]*a)
            return(output)
        except:
            print("Zły format skalara")
        

    
    def rand_gen(self):
        """
        Funkcja rand_gen
        
        Parametry: brak
        
        Output: wypełnia listę reprezentującą wektor losowymi wartościami """
        for i in range(0, len(self.vector)):
            self.vector[i] = rand(-100,100)

    def impl_list(self, list):
        """
        Funkcja impl_list
        
        Parametry: list - lista 
        
        Output: wypełnia listę reprezentującą wektor losowymi wartościami """
        if len(self.vector) != len(list):
            print("różne rozmiary wektora!")
        else:
            try:
                for i in range(0,len(list)):                
                    self.vector[i] = int(list[i])
            except:
                print("Zły format listy")
    
    def length(self):
        """
        Funkcja length
        
        Parametry: brak
        
        Output: zwraca długość wektora reprezentowanego w formie listy """
        x = self.vector[0]
        y = self.vector[1]
        z = self.vector[2]
        l = math.sqrt(x**2 + y**2 + z**2)
        return(l)
    
    def sum_elem(self):
        """
        Funkcja sum_elem
        
        Parametry: brak
        
        Output: zwraca sumę elementów vectora """
        suma = 0
        for i in range(0,len(self.vector)):
            suma += self.vector[i]
        return suma


    def iloc_skal(self, vector2):
        """
        Funkcja iloc_skal
        
        Parametry: vector2 - jest w postaci listy, krotki lub klasy Vector
        
        Output: zwraca iloczyn skalarny self.vector x vector2"""
        if type(vector2) == Vector:
            if len(self.vector) == len(vector2.vector):
                output = 0
                for i in range(0,len(self.vector)):
                   output += self.vector[i] * vector2.vector[i]
                return(output)
            else:
                raise ValueError("Różne wymiary!")
        else:
            if len(self.vector) == len(vector2):
                output = 0
                for i in range(0,len(self.vector)):
                   output+= self.vector[i] * vector2[i]
                return(output)
            else:
                raise ValueError("Różne wymiary!")
    

if(__name__ == "__main__"):
    v = Vector()
    u = Vector()
    v.impl_list([1,2,3])
    u.impl_list([1,2,3])

    print(v[0],v[-1], v[2])
    v[0] = 3
    print(v[0],v[-1], v[2])
    print(4 in v)