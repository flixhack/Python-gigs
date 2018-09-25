import tkinter as tk



print(ord("b"))
print(chr(98))




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

keyEntry=tk.Entry(window)
keyEntry.place(x=155, y= 100)
keyLabel=tk.Label(window, text="Key")
keyLabel.place(x=155, y=130)





window.mainloop()
