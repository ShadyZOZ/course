from Tkinter import *

def encrypt():
    result = ''
    if step.get() == 'input step here (default: 3)':
        shift = 3
    else:
        shift = int(step.get())

    for char in plaintext.get():
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(97 + ((ord(char)+shift) - 97)%26)
        if ord(char) >= 65 and ord(char) <= 90:
            result += chr(65 + ((ord(char)+shift) - 65)%26)
        if ord(char) >= 48 and ord(char) <= 57:
            result += chr(48 + ((ord(char)+shift) - 48)%10)
        if ord(char) >= 33 and ord(char) <= 47:
            result += chr(33 + ((ord(char)+shift) - 33)%15)
        if ord(char) >= 58 and ord(char) <= 64:
            result += chr(58 + ((ord(char)+shift) - 58)%7)
        if ord(char) >= 91 and ord(char) <= 96:
            result += chr(91 + ((ord(char)+shift) - 91)%6)
        if ord(char) >= 123 and ord(char) <= 126:
            result += chr(123 + ((ord(char)+shift) - 123)%4)
        if char == ' ':
            result += ' '
    EncryptResult.set(result)

def decrypt():
    result = ''
    if step.get() == 'input step here (default: 3)':
        shift = 3
    else:
        shift = int(step.get())

    for char in EncryptResult.get():
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(122 - (122 - (ord(char)-shift))%26)
        if ord(char) >= 65 and ord(char) <= 90:
            result += chr(90 - (90 - (ord(char)-shift))%26)
        if ord(char) >= 48 and ord(char) <= 57:
            result += chr(57 - (57 - (ord(char)-shift))%10)
        if ord(char) >= 33 and ord(char) <= 47:
            result += chr(47 - (47 - (ord(char)-shift))%15)
        if ord(char) >= 58 and ord(char) <= 64:
            result += chr(64 - (64 - (ord(char)-shift))%7)
        if ord(char) >= 91 and ord(char) <= 96:
            result += chr(96 - (96 - (ord(char)-shift))%6)
        if ord(char) >= 123 and ord(char) <= 126:
            result += chr(126 - (126 - (ord(char)-shift))%4)
        if char == ' ':
            result += ' '
    DecryptResult.set(result)

def about():
    a = [72, 97, 99, 107, 101, 100, 32, 98, 121, 32, 83, 104, 97, 100, 121, 95, 49, 51, 48, 56, 52, 49, 50, 51]
    key = ''
    for i in a:
        key += chr(i)
    about = Label(root,text=key)
    about.pack(side=BOTTOM)

root = Tk()
root.title("The Caesar Cipher - python")
root.geometry('600x400')

head = Label(root,text="The Caesar Cipher")
head.pack(side=TOP)

# menubar for fun
menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=filemenu)

# step
step = StringVar()
entry = Entry(root,textvariable = step, width=80)
step.set('input step here (default: 3)')
entry.pack()

# plaintext input
plaintext = StringVar()
entry = Entry(root,textvariable = plaintext, width=80)
plaintext.set('input plaintext here')
entry.pack()

# encrypt button
Button(root, text="encrypt", fg="blue",bd=2,width=20,command=encrypt).pack()

# encrypt result
EncryptResult = StringVar()
Entry(root, width=80, textvariable=EncryptResult).pack()
EncryptResult.set('encrypt result / input cyphertext here')

# decrypt button
Button(root, text="decrypt", fg="blue",bd=2,width=20,command=decrypt).pack()

# decrypt result
DecryptResult = StringVar()
Entry(root, width=80, textvariable=DecryptResult, stat="readonly").pack()
DecryptResult.set('decrypt result')

# enable menubar
root.config(menu=menubar)

root.mainloop()
