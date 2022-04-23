import random, timeit


a = []

for i in range (10_000):
    num = random.randint(-100_000_0,100_000_0)
    a.append(num)
def bubble_sort(a):
    N = len(a)
    for i in range(0,N-1):
        for j in range(0, N-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

#===================================
start = timeit.default_timer()
bubble_sort(a)
stop = timeit.default_timer()
execution_time = stop - start
print("Program Executed in "+str(execution_time))
#===================================