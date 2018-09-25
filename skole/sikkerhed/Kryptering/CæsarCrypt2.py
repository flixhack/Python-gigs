import tkinter as tk



print(ord("b"))
print(chr(98))

global keyA
global keyB
global keyC

keyA = 0
keyB = 0
keyC = 0


keyList = [keyA, keyB, keyC]
def setKeys():
    global keyA
    global keyB
    global keyC
    keyA = int(keyAEntry.get())
    keyB = int(keyBEntry.get())
    keyC = int(keyCEntry.get())
    print([keyList])

def crypt():
    key = int(keyEntry.get())
    n = 1
    preCif = str(textEntry.get())
    for i in preCif:
        cifInt= ord(i)+key
        cif= chr(cifInt)
        textEntry2.insert(n, str(cif))
        n = n+1

def deCrypt():
    deKey = int(keyEntry.get())
    m = 1
    preDecif = str(deCifEntry.get())
    for p in preDecif:
        deCifInt = ord(p) -deKey
        deCif = chr(deCifInt)
        deCifEntry2.insert(m, str(deCif))
        m = m+1



window=tk.Tk()
window.title("Crypt")
window.config(height=600, width=800)



textEntry=tk.Entry(window)
textEntry.place(x=10, y=10)
textEntry2=tk.Entry(window)
textEntry2.place(x=10, y=40)
ciphyButton=tk.Button(window, text="krypter", command=crypt)
ciphyButton.place(x=145, y=9)
ciphyButton.config(height=1, width=6)



deCifEntry=tk.Entry(window)
deCifEntry.place(x=300, y=10)
deCifEntry2=tk.Entry(window)
deCifEntry2.place(x=300, y=40)
deCiphyButton=tk.Button(window, text="Dekryp", command=deCrypt)
deCiphyButton.place(x=435, y=9)
deCiphyButton.config(height=1, width=6)

keyAEntry=tk.Entry(window)
keyAEntry.place(x=155, y= 100)
keyALabel=tk.Label(window, text="KeyA")
keyALabel.place(x=155, y=130)
keyBEntry=tk.Entry(window)
keyBEntry.place(x=155, y= 160)
keyBLabel=tk.Label(window, text="KeyB")
keyBLabel.place(x=155, y=190)
keyCEntry=tk.Entry(window)
keyCEntry.place(x=155, y= 220)
keyCLabel=tk.Label(window, text="KeyC")
keyCLabel.place(x=155, y=250)

keyButton=tk.Button(window, text="Set Keys", command=setKeys)
keyButton.place(x=300, y=155)
keyButton.config(height=1, width=5)


window.mainloop()
