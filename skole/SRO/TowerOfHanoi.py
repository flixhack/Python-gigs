import time

def hanoi(n, source, helper, target):
    if n > 0:
     # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
 # move disk from source peg to target peg
        if source:
            target.append(source.pop())
     # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)

def starthanoi(n):
    print("Running n =",n)
    source = []
    target = []
    helper = []
 # create tower on source peg
    for i in range(n, 0, -1):
        source.append(i)
 # start timer
    timer = time.time()
 # run towers of hanoi with problem of size n
    hanoi(len(source), source, helper, target)
 # stop timer
    timer = time.time() - timer
    file.write(str(timer)+"\n ")
    print("Time to complete in seconds:",timer)

for q in range(5):
    file = open("list2.txt","a")
    for i in range(1, 26):
        starthanoi(i)
    file.write("----------\n \n")
    file.close()
