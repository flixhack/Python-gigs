from random import randint
from time import time

def insertionSort(arr):
    print("Length of the list:", n)
    clearList()
    makeList(n)
    timer = time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    timer = time()-timer
    print ("Time to sort the list:",timer )
    file.write(str(timer)+"\n")

def clearList():
    for i in range(len(arr)):
        arr.pop()

def makeList(n):
    for i in range(n):
        arr.append(randint(0,100))


for q in range(5):
    n=2000
    arr=[]
    file = open("list.txt", "a")
    for i in range(10):
        insertionSort(arr)
        n = n+500
    file.write("--------\n \n")
    file.close()
