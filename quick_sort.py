import random, timeit

random_num = 1_000_000
a = []

for i in range (random_num):
    num = random.randint(-100_000_0,100_000_0)
    a.append(num)


def merge(a, b):

    c = []
    m = len(a)
    n = len (b)

    i = 0
    j = 0

    while i < m and j < n:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    #print (c)
    return c

def split(a):
    N1 = len(a) // 2
    a1 = a[N1:]
    a2 = a[:N1]

    if len(a1) > 1:
        a1 = split(a1)
    if len(a2) > 1:
        a2 = split(a2)

    return merge(a1,a2)

#===================================
start = timeit.default_timer()
a = split(a)
stop = timeit.default_timer()
execution_time = stop - start
print("Program Executed in "+str(execution_time))
#===================================


a = []

for i in range (random_num):
    num = random.randint(-100_000_0,100_000_0)
    a.append(num)

#===================================
start = timeit.default_timer()
a.sort()
stop = timeit.default_timer()
execution_time = stop - start
print("Program Executed in "+str(execution_time))
#===================================