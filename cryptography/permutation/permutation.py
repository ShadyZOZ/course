from Tkinter import *

def encrypt():
	x = 0
	EncryptKey = (2, 5, 8, 6, 1, 3, 7, 4)
	EncryptText = plaintext.get()
	result = EncryptText
	if len(result) % 8 != 0:
		result += EncryptText[:len(result) % 8]
		EncryptText = result
	for char in EncryptText:
		key = EncryptKey[x % 8]
		order = key + 8 * (x / 8) - 1
		result = result[:order] + char + result[order+1:]
		x += 1
	EncryptResult.set(result)

def decrypt():
	x = 0
	DecryptKey = (5, 1, 6, 8, 2, 4, 7, 3)
	result = EncryptResult.get()
	for char in EncryptResult.get():
		key = DecryptKey[x % 8]
		order = key + 8 * (x / 8) - 1
		result = result[:order] + char + result[order+1:]
		x += 1
	DecryptResult.set(result[:len(plaintext.get())])

# personal signature for fun
def about():
    a = [72, 97, 99, 107, 101, 100, 32, 98, 121, 32, 83, 104, 97, 100, 121, 95, 49, 51, 48, 56, 52, 49, 50, 51]
    key = ''
    for i in a:
        key += chr(i)
    about = Label(root,text=key)
    about.pack(side=BOTTOM)

root = Tk()
root.title("The Permutation cipher - python")
root.geometry('600x400')

head = Label(root,text="The Permutation Cipher")
head.pack(side=TOP)

# menubar for fun
menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=filemenu)

# plaintext input
plaintext = StringVar()
entry = Entry(root,textvariable = plaintext, width=80)
plaintext.set('input plaintext here')
entry.pack()

# encrypt button
Button(root, text="encrypt", fg="blue",bd=2,width=20,command=encrypt).pack()

# encrypt result
EncryptResult = StringVar()
Entry(root, width=80, textvariable=EncryptResult, stat="readonly").pack()
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
