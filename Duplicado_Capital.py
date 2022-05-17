"""MESES PARA DUPLICAR SU CAPITAL"""

from tkinter import N


C = int(input("Ingrese su Capital inicial: "))
B = 2*C
N = 0

while C < B:
    
    N = N + 1
    
    C = C + (C*0.05)

print("El tiempo necesario es de " + str(N) + " meses")