password="zzzz"

start = 97
last = 122
tryWord=""
a = 97
b = 97
c = 97
aa = 97

while tryWord != password:
    tryWord = str(chr(aa)+ chr(a)+chr(b)+chr(c))
    if c < 122:
        c = c + 1
    else:
        c =97
        b = b + 1
    if b > 122:
        b = 97
        a = a + 1
    if a > 122:
        a = 97
        aa = aa + 1


if tryWord==password:
    print("Cracked password = " + tryWord)
