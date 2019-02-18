import tkinter  # importer hele tkinter biblioteket, dog skal man skrive "tkinter.denCommandDuVilSkrive"
import math  # importer hele math biblioteket, dog skal man skrive "math.denCommandDuVilSkrive"


# forkellige brugte variabler:
# global 'a'
# global 'b'
# global 'c'
# global 'd'
# global 'z'
# Local 'x' brugt i equal
# local 'sr' brugt i kvadratrod
# local 'cc' brugt i cos
# local 'sinc' brugt i sin
# local 'tc' brugt i tan


def udregn():
    if udr == 0:
        udr = float(firstEntry.get())  # kopier det der står i entry ned til a
        firstEntry.delete(0, 1000)  # sletter det der står i entry
    elif a != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(a + x))
        a = 0
        z = 0
    elif b != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(b - x))
        b = 0
        z = 0
    elif c != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(c * x))
        c = 0
        z = 0
    elif d != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(d / x))
        d = 0
        z = 0


global z
z = 0

# Laver fire globaler variabler til + - ÷ x og sætter variablerne til 0.
global a
global b
global c
global d
a = 0
b = 0
c = 0
d = 0


#
# Herunder har vi de forskellige kommandoer de forskellige knapper.
def addButton():
    global a  # Siger at i denne funktion bruger vi global a, b, c, d og z
    global b
    global c
    global d
    global z
    z = 0
    if a == 0:
        a = float(firstEntry.get())  # kopier det der står i entry ned til a
        firstEntry.delete(0, 1000)  # sletter det der står i entry
    elif a != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(a + x))
        a = 0
        z = 0
    elif b != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(b - x))
        b = 0
        z = 0
    elif c != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(c * x))
        c = 0
        z = 0
    elif d != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(d / x))
        d = 0
        z = 0


def subButton():
    global a  # Siger at i denne funktion bruger vi global a
    global b
    global c
    global d
    global z
    z = 0
    if b == 0:
        b = float(firstEntry.get())  # kopier det der står i entry ned til a
        firstEntry.delete(0, 1000)  # sletter det der står i entry
    elif a != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(a + x))
        a = 0
        z = 0
    elif b != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(b - x))
        b = 0
        z = 0
    elif c != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(c * x))
        c = 0
        z = 0
    elif d != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(d / x))
        d = 0
        z = 0


def multiplyButton():
    global a  # Siger at i denne funktion bruger vi global a
    global b
    global c
    global d
    global z
    z = 0
    if c == 0:
        c = float(firstEntry.get())  # kopier det der står i entry ned til a
        firstEntry.delete(0, 1000)  # sletter det der står i entry
    elif a != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(a + x))
        a = 0
        z = 0
    elif b != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(b - x))
        b = 0
        z = 0
    elif c != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(c * x))
        c = 0
        z = 0
    elif d != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(d / x))
        d = 0
        z = 0


def divideButton():
    global a  # Siger at i denne funktion bruger vi global a
    global b
    global c
    global d
    global z
    z = 0
    if d == 0:
        d = float(firstEntry.get())  # kopier det der står i entry ned til a
        firstEntry.delete(0, 1000)  # sletter det der står i entry
    elif a != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(a + x))
        a = 0
        z = 0
    elif b != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(b - x))
        b = 0
        z = 0
    elif c != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(c * x))
        c = 0
        z = 0
    elif d != 0:
        x = float(firstEntry.get())
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(d / x))
        d = 0
        z = 0


def sqrtCommand():
    global z
    sr = 0
    sr = float(firstEntry.get())
    if sr >= 0:
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(math.sqrt(sr)))
    else:
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, "i")
    z = 0


def cosCommand():
    global z
    cc = 0
    cc = float(firstEntry.get())
    firstEntry.delete(0, 1000)
    firstEntry.insert(1, str(math.cos(cc)))
    z = 7
    firstEntry.delete(7, 1000)


def sinCommand():
    global z
    sinc = 0
    sinc = float(firstEntry.get())
    firstEntry.delete(0, 1000)
    firstEntry.insert(1, str(math.sin(sinc)))
    z = 7
    firstEntry.delete(7, 1000)


def tanCommand():
    global z
    tc = 0
    tc = float(firstEntry.get())
    firstEntry.delete(0, 1000)
    firstEntry.insert(1, str(math.tan(tc)))
    z = 7
    firstEntry.delete(7, 1000)


def fakCommand():
    fc = 0
    fc = int(firstEntry.get())
    firstEntry.delete(0, 1000)
    firstEntry.insert(1, str(math.factorial(fc)))


def piCommand():
    global z
    firstEntry.insert(1, str(math.pi))
    z = 20
    firstEntry.delete(20, 1000)


def equalButton():
    global a  # Siger at i denne funktion bruger vi global a, b, c, d.
    global b
    global c
    global d
    global z
    x = float(firstEntry.get())  # kopier det der står i entry ned til x
    if a != 0:  # Her tjekker vi om a, b, c og d skulle være lig med 0 og ud fra
        firstEntry.delete(0, 1000)  # det bestemmer om vi skal plus, minus, gange
        firstEntry.insert(1, str(a + x))  # eller dividere, og derefter skriver
        a = 0  # resultatet i vores entry
        z = 0
    elif b != 0:
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(b - x))
        b = 0
        z = 0
    elif c != 0:
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(c * x))
        c = 0
        z = 0
    elif d != 0:
        firstEntry.delete(0, 1000)
        firstEntry.insert(1, str(d / x))
        d = 0
        z = 0


# Herunder er alle tal knappernes funktioner.
def zeroButton():
    global z
    z = z + 1
    firstEntry.insert(1000, "0")


def oneButton():
    global z
    z = z + 1
    firstEntry.insert(1000, "1")


def twoButton():
    global z
    z = z + 1
    firstEntry.insert(1000, "2")


def threeButton():
    global z
    z = z + 1
    firstEntry.insert(1000, "3")


def fourButton():
    global z
    z = z + 1
    firstEntry.insert(1000, "4")


def fiveButton():
    global z
    z = z + 1
    firstEntry.insert(1000, "5")


def sixButton():
    global z
    z = z + 1
    firstEntry.insert(1000, "6")


def sevenButton():
    global z
    z = z + 1
    firstEntry.insert(1000, "7")


def eightButton():
    global z
    z = z + 1
    firstEntry.insert(1000, "8")


def nineButton():
    global z
    z = z + 1
    firstEntry.insert(1000, "9")


def commaButton():
    global z
    z = z + 1
    firstEntry.insert(1000, ".")


# herunder de to delete knapper.
def allClearButton():
    firstEntry.delete(0, 1000)
    global a
    global b
    global c
    global d
    global z
    a = 0
    b = 0
    c = 0
    d = 0
    z = 0


def clearButton():
    global z
    firstEntry.delete(z - 1, z + 1)
    if z > 0:
        z = z - 1
    else:
        pass


def hej():  # Bruger til at teste knapperne
    print('hej')


window = tkinter.Tk()  # Det her er selve vinduet
window.title("Lommeregner")
# window = tkinter.Toplevel(height = 230, width = 300)
window["height"] = 225
window["width"] = 300

helloLabel = tkinter.Label(window, text="Lommeregner")  # Det her er det lille tekststykke der siger lommeregner
helloLabel.place(x=55, y=5)

firstEntry = tkinter.Entry(window, bd=10)  # Her har vi så kassen der skrives i
firstEntry.place(x=25, y=30)

addButton1 = tkinter.Button(window, text="+", command=addButton)  # Det her er plusknappen
addButton1.place(x=110, y=70)
addButton1.config(height=1, width=2)

subButton1 = tkinter.Button(window, text="-", command=subButton)  # det her er minusknappen
subButton1.place(x=110, y=100)
subButton1.config(height=1, width=2)

multiplyButton1 = tkinter.Button(window, text="x", command=multiplyButton)  # det her er gange knappen
multiplyButton1.place(x=110, y=130)
multiplyButton1.config(height=1, width=2)

divideButton1 = tkinter.Button(window, text="÷", command=divideButton)  # Det her er divider knappen
divideButton1.place(x=110, y=160)
divideButton1.config(height=1, width=2)

sqrtButton = tkinter.Button(window, text="√", command=sqrtCommand)  # Det her er kvadratrod knappen
sqrtButton.place(x=170, y=70)
sqrtButton.config(height=1, width=2)

cosButton = tkinter.Button(window, text="cos", command=cosCommand)  # Det her er cos knappen
cosButton.place(x=170, y=100)
cosButton.config(height=1, width=2)

sinButton = tkinter.Button(window, text="sin", command=sinCommand)  # Det her er sin knappen
sinButton.place(x=170, y=130)
sinButton.config(height=1, width=2)

tanButton = tkinter.Button(window, text="tan", command=tanCommand)  # Det her er tan knappen
tanButton.place(x=170, y=160)
tanButton.config(height=1, width=2)

fakButton = tkinter.Button(window, text="!", command=fakCommand)
fakButton.place(x=170, y=190)
fakButton.config(height=1, width=2)

piButton = tkinter.Button(window, text="π", command=piCommand)
piButton.place(x=200, y=70)
piButton.config(height=1, width=2)

equalButton1 = tkinter.Button(window, text="=", command=equalButton)  # Det her er lig med knappen
equalButton1.place(x=140, y=70)
equalButton1.config(height=7, width=2)

allClearButton = tkinter.Button(window, text="ac", command=allClearButton)  # Knappen der sletter alt i entry
allClearButton.place(x=95, y=190)
allClearButton.config(height=1, width=8)

ClearButton1 = tkinter.Button(window, text="c", command=clearButton)
ClearButton1.place(x=25, y=190)
ClearButton1.config(height=1, width=8)

# tal knappernes interface.
oneButton1 = tkinter.Button(window, text="1", command=oneButton)
oneButton1.place(x=20, y=70)
oneButton1.config(height=1, width=2)
twoButton1 = tkinter.Button(window, text="2", command=twoButton)
twoButton1.place(x=50, y=70)
twoButton1.config(height=1, width=2)
threeButton1 = tkinter.Button(window, text="3", command=threeButton)
threeButton1.place(x=80, y=70)
threeButton1.config(height=1, width=2)
fourButton1 = tkinter.Button(window, text="4", command=fourButton)
fourButton1.place(x=20, y=100)
fourButton1.config(height=1, width=2)
fiveButton1 = tkinter.Button(window, text="5", command=fiveButton)
fiveButton1.place(x=50, y=100)
fiveButton1.config(height=1, width=2)
sixButton1 = tkinter.Button(window, text="6", command=sixButton)
sixButton1.place(x=80, y=100)
sixButton1.config(height=1, width=2)
sevenButton1 = tkinter.Button(window, text="7", command=sevenButton)
sevenButton1.place(x=20, y=130)
sevenButton1.config(height=1, width=2)
eightButton1 = tkinter.Button(window, text="8", command=eightButton)
eightButton1.place(x=50, y=130)
eightButton1.config(height=1, width=2)
nineButton1 = tkinter.Button(window, text="9", command=nineButton)
nineButton1.place(x=80, y=130)
nineButton1.config(height=- 1, width=2)
zeroButton1 = tkinter.Button(window, text="0", command=zeroButton)
zeroButton1.place(x=51, y=160)
zeroButton1.config(height=1, width=6)
commaButton1 = tkinter.Button(window, text=",", command=commaButton)
commaButton1.place(x=20, y=160)
commaButton1.config(height=1, width=2)

# Herunder er de forskellige keybinds så man kan bruge numpad til at regne med.
window.bind('<Return>', lambda event: equalButton())

window.bind('<BackSpace>', lambda event: clearButton())

window.bind('+', lambda event: addButton())
window.bind('-', lambda event: subButton())
window.bind('*', lambda event: multiplyButton())
window.bind('/', lambda event: divideButton())

window.bind(',', lambda event: commaButton())
window.bind('0', lambda event: zeroButton())
window.bind('1', lambda event: oneButton())
window.bind('2', lambda event: twoButton())
window.bind('3', lambda event: threeButton())
window.bind('4', lambda event: fourButton())
window.bind('5', lambda event: fiveButton())
window.bind('6', lambda event: sixButton())
window.bind('7', lambda event: sevenButton())
window.bind('8', lambda event: eightButton())
window.bind('9', lambda event: nineButton())
