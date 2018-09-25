import time
import random
import numpy as np
import matplotlib.pyplot as plt

## Helper functions START ##
def built_in_time(L):

    start = time.time()
    L.sort()
    end = time.time()
    return end - start
def bubble(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j + 1]
                a[j + 1] = a[j]
                a[j] = temp
    return a
def bubble_time(L):
    start = time.time()
    bubble(L)
    end = time.time()
    return end - start
def merge(L1,L2):
    L = []
    while (len(L1) != 0 and len(L2) != 0):
        if L1[0] < L2[0]:
            L.append(L1[0])
            L1.remove(L1[0])
        else:
            L.append(L2[0])
            L2.remove(L2[0])
    if len(L1) == 0:
        L += L2
    else:
        L += L1
    return L
def mergesort(L):
    if len(L) == 0 or len(L) == 1:
        return L
    else:
        m = int(len(L) / 2)
        L1 = L[:m]
        L2 = L[m:]
        return merge(mergesort(L1), mergesort(L2))
def merge_time(L):
    start = time.time()
    mergesort(L)
    end = time.time()
    return end - start

## Helper functions END ##

size2 =  np.array([10 * i for i in range(100)])

a = []
b = []
c = []

for n in size2:
    L = [random.randint(1,100) for i in range(n)]
    a.append(built_in_time(L))
    b.append(bubble_time(L))
    c.append(merge_time(L))


fig, ax = plt.subplots(figsize = (40,40))
ax.plot(size2, a, linewidth = 3, label = 'Built-in')
ax.plot(size2, b, linewidth = 3, label = 'Bubble')
ax.plot(size2, c, linewidth = 3, label = 'Merge')
plt.xlabel("Size of the LIST")
plt.ylabel("Time")
plt.title("Time versus Size")
plt.legend(loc = 'upper left', prop={'size': 20})
plt.grid(True)
plt.show()