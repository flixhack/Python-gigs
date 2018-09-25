n = 6971
g = 1471


a = 612
b = 917


ag = g**a%n
bg = g**b%n


bag = ag**b%n
abg = bg**a%n


print(ag)
print(bg)


print(bag)
print(abg)
