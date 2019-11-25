import sympy as sym
import numpy as np 
import math as m 
import sys

def Coeff(n, Rov):
    try:
        n = int(n)
        Rov = float(Rov)
    except:
        print('N should be an integer and R0v a number')
        return
    z0 = m.cosh(1/n * m.acosh(Rov))
    X = z0**2 - 1
    A = []
    value1 = 0
    end = round(n/2)
    for k in range(int(n/2), n, 1):
        for i in range(1,k+1,1):
            value1 += X**i*(m.factorial(n-2-k+i)/(m.factorial(i)*m.factorial(i-1)*m.factorial(k-i)))
        value = z0**(n-1-(2*k))*(m.factorial(k-1)/m.factorial(n-1-k))*value1
        value1 = 0
        A.append(value)
    
    printCoeff(np.divide(A, min(A)))

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

