from Tkinter import *
from table import *
import random, string

SubKey = [[0] * 48] * 16

# byte2bit
def byte2bit(inChar, outBit):
    inChar = [ord(c) for c in inChar]
    pos = 0
    for ch in inChar:
        i = 7
        while i >= 0:
            if ch & (1 << i) != 0:
                outBit[pos] = 1
            else :
                outBit[pos] = 0
            pos += 1
            i -= 1

# bit2byte
def bit2byte(inBit):
    result = []
    s = i = 0
    for x in inBit:
        s += s + int(x)
        i += 1
        if i == 8:
            result.append(chr(s))
            s = i = 0
    if i > 0:
        result.append(chr(s << (8 - i)))
    return result

# table transform
def TransForm(inBit, table, length):
    outBit = []
    for i in range(length):
        outBit.append(inBit[table[i] - 1])
    return outBit

# generate subkeys
def SetSubKey(key):
    k = [0] * 64
    byte2bit(key, k)
    k = TransForm(k, PC1_Table, 56)
    kL = k[0:28]
    kR = k[28:56]
    for i in range(16):
        kL = RotateL(kL, LOOP_Table[i])
        kR = RotateL(kR, LOOP_Table[i])
        K = kL + kR
        SubKey[i] = TransForm(K, PC2_Table, 48)

# left shift
def RotateL(key, loop):
    keyOut = key[loop:] + key[:loop]
    return keyOut

# xor
def Xor(InA, InB):
    Out = []
    for i in range(len(InA)):
        Out.append(InA[i] ^ InB[i])
    return Out

# s_box
def S_func(In):
    result = []
    for i in range(8):
        x = In[(0 + i * 6):(6 + i * 6)]
        j = int(str(x[0] * 10 + x[5]), 2)
        k = int(str(x[1] * 1000 + x[2] * 100 + x[3] * 10 + x[4]), 2)
        Out = bin(S[i][j][k])[2:]
        if len(Out) != 4:
            Out = '0' * (4 - len(Out)) + Out
        for b in Out:
            result.append(int(b))
    return result

# f_function
def F_func(In, Ki):
    MR = TransForm(In, E_Table, 48)
    MR = Xor(MR, Ki)
    Out = S_func(MR)
    Out = TransForm(Out, P_Table, 32)
    return Out

def single_encrypt(plain):
    plainbit = [0] * 64
    byte2bit(plain, plainbit)
    plainbit = TransForm(plainbit, IP_Table, 64)
    Li = plainbit[:32]
    Ri = plainbit[32:]
    for i in range(16):
        F_R = F_func(Ri, SubKey[i])
        Rnext =Xor(Li, F_R)
        Li = Ri
        Ri = Rnext
    plainbit = Li + Ri
    plainbit = TransForm(plainbit, IP_R_Table, 64)
    result = ''
    for bit in plainbit:
        result += str(bit)
    return result

def single_decrypt(bit):
    cypherbit = []
    for b in bit:
        cypherbit.append(int(b))
    cypherbit = TransForm(cypherbit, IP_Table, 64)
    Li = cypherbit[:32]
    Ri = cypherbit[32:]
    for i in range(16):
        F_L = F_func(Li, SubKey[15 - i])
        Lnext =Xor(Ri, F_L)
        Ri = Li
        Li = Lnext
    decypherbit = Li + Ri
    decypherbit = TransForm(decypherbit, IP_R_Table, 64)
    decyphertext = bit2byte(decypherbit)
    result = ''
    for char in decyphertext:
        result += str(char)
    return result

def encrypt():
    if len(key.get()) != 8:
        EncryptResult.set('please input 8 byte key!')
        return
    SetSubKey(key.get())
    result = ''
    t = len(plaintext.get()) / 8 + ((len(plaintext.get()) % 8) > 0)
    for i in range(t):
        result += single_encrypt(plaintext.get()[8 * i : 8 * (i + 1)])
    EncryptResult.set(result)

def decrypt():
    t = len(EncryptResult.get()) / 64
    result = ''
    for i in range(t):
        result += single_decrypt(EncryptResult.get()[64 * i : 64 * (i + 1)])
    DecryptResult.set(result)

# random key
def RandomKey():
    rKey = random.sample(string.letters+string.digits, 8)
    k = ''
    for elem in rKey:
        k += elem
    key.set(k)

# for fun
def about():
    about = Label(root,text='hacked by Shady')
    about.pack(side=BOTTOM)

root = Tk()
root.title("DES")
root.geometry('600x400')

head = Label(root,text="DES")
head.pack(side=TOP)

# menubar for fun
menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=filemenu)

# key
key = StringVar()
Entry(root,textvariable = key, width=80).pack()
key.set('input 8 byte key here')

# random key
Button(root, text="random key", fg="blue",bd=2,width=20,command=RandomKey).pack()

# plaintext input
plaintext = StringVar()
entry = Entry(root,textvariable = plaintext, width=80).pack()
plaintext.set('input plaintext here')

# encrypt button
Button(root, text="encrypt", fg="red",bd=2,width=20,command=encrypt).pack()

# encrypt result
EncryptResult = StringVar()
Entry(root, width=80, textvariable=EncryptResult).pack()
EncryptResult.set('encrypt result / input cyphertext here')

# decrypt button
Button(root, text="decrypt", fg="green",bd=2,width=20,command=decrypt).pack()

# decrypt result
DecryptResult = StringVar()
Entry(root, width=80, textvariable=DecryptResult, stat="readonly").pack()
DecryptResult.set('decrypt result')

# enable menubar
root.config(menu=menubar)

root.mainloop()
