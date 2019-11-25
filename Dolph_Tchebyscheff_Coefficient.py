import sympy as sym
import math as m
import numpy as np
import sys

def Coeff(n,Rov):
    try:
        n = int(n)
        Rov = float(Rov)
    except:
        print('N should be an integer and R0v a number')
        return
    
    AFn = 0
    Tn = []
    c = []
    Solve = []
    Solve1 = []
    j = 0
    x = sym.Symbol('x')
    Tn.append(1)
    Tn.append(x)
    for i in range(2,n+1):
        Tn.append(sym.expand(2*x*Tn[i-1] - Tn[i-2]))
    #print(Tn)
    z0 = m.cosh(1/n * m.acosh(Rov))
    #print(z0)
    if n % 2:
        #dispari
        for i in range(1,n+1,2):
            c.append(sym.Symbol('a%d'%(j)))
            AFn += Tn[i]*c[j]
            #print(AFn)
            j = j + 1

        #print(sym.expand(AFn))
        a = sym.Poly(AFn, x)
        b = sym.Poly(Tn[n],x)
        acoeff = a.coeffs()
        bcoeff = b.coeffs()
        #print(acoeff)
        #print(bcoeff)
        for i in range(0,len(acoeff)):
            coefftemp = bcoeff[len(bcoeff) - i - 1]*(z0**(2*i+1))
            Solve.append(acoeff[len(acoeff) - i - 1] - coefftemp)
        #print(Solve)
        Result = sym.solve(Solve, c)
        #print(Result)
        lista1 = list(Result.values())
        printCoeff(np.divide(lista1, min(lista1)))
        #define the array factor for even
        #print("odd")
    else:
        #pari
        for i in range(2,n+2,2):
            c.append(sym.Symbol('a%d'%(j)))
            AFn += Tn[i]*c[j]
            #print(AFn)
            j = j + 1

        a = sym.Poly(AFn, x)
        b = sym.Poly(Tn[n], x)
        acoeff = a.coeffs()
        bcoeff = b.coeffs()
        #print(acoeff)
        #print(bcoeff)

        for i in range(1,len(acoeff)):
            coefftemp = bcoeff[len(bcoeff) - i - 1]*(z0**(2*i+1))
            Solve1.append(acoeff[len(acoeff) - i - 1] - coefftemp)
        Result1 = sym.solve(Solve1, c)
        
        #print(Result1)
        lista2 = list(Result1.values())
        printCoeff(np.divide(lista2, min(lista2)))
        #define AF for odd

def printCoeff(coe):
    if len(coe) % 2:
        #dispari
        for i in range(0, len(coe)):
            print('a{}\t\t{}'.format(len(coe)-i-1 ,coe[len(coe)-i-1]))
        for i in range(1, len(coe)):
            print('a{}\t\t{}'.format(i ,coe[i]))
    else:
        #pari
        for i in range(0, len(coe)):
            print('a{}\t\t{}'.format(len(coe)-i-1 ,coe[len(coe)-i-1]))
        for i in range(0, len(coe)):
            print('a{}\t\t{}'.format(i ,coe[i]))


def main(argv):
    if len(argv) == 2:
        Coeff(argv[0], argv[1])
    else:
        Coeff(input('Inserisci numero di elementi:'), input('Inserisci R0v:'))


if __name__ == "__main__":
   main(sys.argv[1:])