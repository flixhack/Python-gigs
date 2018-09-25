password="zzzz"

PWL = len(password)
tryWord=""

n = 97
# for i in range(PML):
#     chr(n)
#
#     n = n + 1
#
# for i in range(PWL):
#     tryWord = tryWord + str(chr(97))
#     print(tryWord)


for i in range(PWL):
    q = 0
    if q >= PWL:
        tryWord = tryWord + str(chr(97))
    else:
        tryWord = tryWord + str(chr(97+1))






while tryWord != password:
        pass







if tryWord==password:
        print("Cracked password = " + tryWord)






# start = 97
# last = 122
# tryWord=""
# a = 97
# b = 97
# c = 97
# aa = 97
#
#
# while tryWord != password:
#     tryWord = str(chr(aa)+ chr(a)+chr(b)+chr(c))
#     if c < 122:
#         c = c + 1
#     else:
#         c =97
#         b = b + 1
#     if b > 122:
#         b = 97
#         a = a + 1
#     if a > 122:
#         a = 97
#         aa = aa + 1
#
#
#
