print("zad1")
import sys
print("Podaj tekst: ")
s = sys.stdin.readline()
sys.stdout.write(s)
a = input("Podaj napis: ")
suma=a.count(" ")
print(suma)

import sys
print("\nzad2")
print("Insert n1: ")
n1 = int(sys.stdin.readline())
print("Insert n2: ")
n2 = int(sys.stdin.readline())
mn = n1*n2
print(mn)

import sys
import math as m
print("\nzad4")
n3 = int(input("Insert n3: "))
print(int (m.fabs(n3)))

import sys
print("\nzad5")
a = int(input("Insert a: "))
b = int(input("Insert b: "))
c = int(input("Insert c: "))
if (a>0 and a<=10) and (a>b or b>c) :
    print("OK")
else:
    print("NOT OK")

print("\nzad6")
for i in range (5, 45, 5):
    print(str(i) + " ")

import sys
print("\nzad7")
for i in range (0, 4, 1):
    x = int(input("Insert the number: "))
    px=x**2
    print(px)

import sys
print("\nzad8")
i=0
lista = []
while (i!= 4):
    x = int(input("Insert x: "))
    lista.append(x)
    i+=1
print(lista)

import sys
print("\nzad9")
suma=0
x = int(input("Insert x: "))
while (x > 0):
        suma += x % 10
        x /= 10
print(int (suma))

import sys
print("\nzad10")
h = int(input("Height: "))
for i in range (1, int(h)+1 ):
    for j in range (1, int(i)+1):
        sys.stdout.write('A')
    sys.stdout.write('\n')

print("\nzad11 - uncompleted")
import sys
import math
H = int(input("Height: "))
s = math.ceil(H/2)

if (H>=3 and H<9 and H%2==1):

    for i in range (1, H+1):
        for j in range (1, H+1):
            if j != s:
                sys.stdout.write(' ')
            else:
                sys.stdout.write('o')
        sys.stdout.write('\n')
else:
    print("ERROR")



