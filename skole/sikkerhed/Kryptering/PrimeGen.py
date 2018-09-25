import tkinter as tk


def prime(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]


def primeGet():
    n=int(numberEntry.get())
    print (prime(n))


window=tk.Tk()
window.title("Primes")
window.config(height=400, width=500)


numberEntry=tk.Entry(window, bd=5)
numberEntry.place(x=200, y=20)

primesButton=tk.Button(window, text="primes", command=primeGet)
primesButton.place(x=340, y=18)


window.mainloop()
