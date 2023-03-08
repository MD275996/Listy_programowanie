from lista1 import Vector

v = Vector()
v.impl_list([1,2,3])

def tworzenie_skalara():
    #kod sprawdzający kropki 1, 2, 3, 
    
    s = Vector(5)
    print(v)
    print(s)

    v.rand_gen()
    print(v)

    v.impl_list([1,2,3,4])
    v.impl_list([1,2,3])
    print(v)

def dodawanie_wektorow():
    #kod sprawdza kropkę 4

    u = Vector()
    u.impl_list([100,100,100])
    print(v+u)
    print(v + [1,2,3,4])

def mnozenie_skalar():

    print(v*12)
    print(v*"asd")

def dlugosc_suma():
    #kod sprawdza kropki 6,7

    print(v.length())
    print(v.sum_elem())

def iloczyn_sk():
    u = Vector()
    u.impl_list([100,100,100])
    print(v.iloc_skal([4,4,4]))
    print(v.iloc_skal(u))

def elementy():
    #kod sprawdza kropki 10, 11
    print(v[0])
    v[0] = 10
    print(v)
    print(10 in v)


v.impl_list([1, 2 ,'c'])
print(v)