import seir 
import sys

#ustawienie domyślnych wartosci
n=1000
s=999
e=1
i=0
r=0
beta = 0.8
sigma = 0.7
gamma = 0.4

tab_arg = sys.argv
tab_arg.remove(tab_arg[0])

if len(tab_arg)%2==0:
    while len(tab_arg)>1:
        arg = tab_arg.pop()
        if 'delta' in arg :
            e = float(tab_arg.pop())
        elif 'sigma' in arg :
            e = float(tab_arg.pop())
        elif 'gamma' in arg :
            e = float(tab_arg.pop())
        elif 'n' in arg or 'N' in arg:
            n = float(tab_arg.pop())
        elif 's' in arg or 'S' in arg:
            s = float(tab_arg.pop())
        elif 'e' in arg or 'E' in arg:
            e = float(tab_arg.pop())
        elif 'i' in arg or 'I' in arg:
            i = float(tab_arg.pop())
        elif 'r' in arg or 'R' in arg:
            e = float(tab_arg.pop())

seir.seir_model(n,s,e,i,r,beta,sigma,gamma)

