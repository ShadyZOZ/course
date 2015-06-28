from Tkinter import *
import random

keyLength = 1024
G_result = []

def fastExpMod(b, e, m):
    result = 1
    while e != 0:
        if (e&1) == 1:
            result = (result * b) % m
        e >>= 1
        b = (b*b) % m
    return result

def primeTest(n):
    q = n - 1
    k = 0
    while q % 2 == 0:
        k += 1;
        q /= 2
    a = random.randint(2, n-2);
    if fastExpMod(a, q, n) == 1:
        return "inconclusive"
    for j in range(0, k):
        if fastExpMod(a, (2**j)*q, n) == n - 1:
            return "inconclusive"
    return "composite"

def findPrime(halfkeyLength):
    while True:
        n = random.randint(0, 1<<halfkeyLength)
        if n % 2 != 0:
            found = True
            for i in range(0, 10):
                if primeTest(n) == "composite":
                    found = False
                    break
            if found:
                return n

def extendedGCD(a, b):
    if b == 0:
        return (1, 0, a)
    x1 = 1
    y1 = 0
    x2 = 0
    y2 = 1
    while b != 0:
        q = a / b
        r = a % b
        a = b
        b = r
        x = x1 - q*x2
        x1 = x2
        x2 = x
        y = y1 - q*y2
        y1 = y2
        y2 = y
    return(x1, y1, a)

def selectE(fn, halfkeyLength):
    while True:
        e = random.randint(0, 1<<halfkeyLength)
        (x, y, r) = extendedGCD(e, fn)
        if r == 1:
            return e

def computeD(fn, e):
    (x, y, r) = extendedGCD(fn, e)
    if y < 0:
        return fn + y
    return y

def RandomKey():
    p = findPrime(keyLength/2)
    q = findPrime(keyLength/2)
    n = p * q
    fn = (p-1) * (q-1)
    e = selectE(fn, keyLength/2)
    d = computeD(fn, e)
    # return (n, e, d)
    N.set(n)
    E.set(e)
    D.set(d)

def encrypt():
    global G_result
    result = []
    for char in plaintext.get():
        result.append(fastExpMod(ord(char), int(E.get()), int(N.get())))
    cyphertext.set(result)
    G_result = result

def decrypt():
    global G_result
    result = ''
    for c in G_result:
        result += (chr(fastExpMod(c, int(D.get()), int(N.get()))))
    decyphertext.set(result)

root = Tk()
root.title("RSA")

Label(root,text="RSA").pack()

fm1 = Frame(root)
fm2 = Frame(root)
fm3 = Frame(root)
fm4 = Frame(root)
fm5 = Frame(root)
fm6 = Frame(root)

Label(fm1, text="n: ").pack(side=LEFT)
N = StringVar()
Entry(fm1, textvariable=N, width=20).pack(side=LEFT)
Label(fm1, text="e: ").pack(side=LEFT)
E = StringVar()
Entry(fm1, textvariable=E, width=20).pack(side=LEFT)
Label(fm1, text="d: ").pack(side=LEFT)
D = StringVar()
Entry(fm1, textvariable=D, width=20).pack(side=LEFT)

Button(fm2, text="random key", fg="blue",bd=2,width=20,command=RandomKey).pack()

Label(fm3, width=15, text="plaintext: ").pack(side=LEFT)
plaintext = StringVar()
Entry(fm3, width=60, textvariable=plaintext).pack(side=LEFT)

Label(fm4, width=15, text="cyphertext: ").pack(side=LEFT)
cyphertext = StringVar()
Entry(fm4, width=60, textvariable=cyphertext).pack(side=LEFT)

Label(fm5, width=15, text="decyphertext: ").pack(side=LEFT)
decyphertext = StringVar()
Entry(fm5, width=60, textvariable=decyphertext).pack(side=LEFT)

Button(fm6, text="encrypt", fg="blue",bd=2,width=20,command=encrypt).pack(side=LEFT)
Button(fm6, text="decrypt", fg="blue",bd=2,width=20,command=decrypt).pack(side=LEFT)

fm1.pack()
fm2.pack()
fm3.pack()
fm4.pack()
fm5.pack()
fm6.pack()

root.mainloop()
