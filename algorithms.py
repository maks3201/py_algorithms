def loop_str():  # writing a loop to a string
    num = [x * x for x in range(10)]
    print(num)


def facktorial(x, sum=1):  # factorials of number
    if x == 1 or x == 0:
        pass
    else:
        sum = sum * x
        return facktorial(x - 1, sum)
    print(sum)


def fibonacci(x):  # fibonacci numbers
    a = 1
    b = 0
    for i in range(x):
        a, b = b, b + a

    print(b)


def reverse_str(x):  # flip a string
    s = list(''.join(x))
    z = -1
    a = 0
    for i in range(len(x) // 2):
        s[a], s[z] = s[z], s[a]
        a += 1
        z -= 1
    x = (''.join(s))
    print(x)


def sel_sort(x):  # selection sort
    n = len(x)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if x[j] < x[i]:
                x[i], x[j] = x[j], x[i]

    return x


def int_sort(x):  # insertion sort
    n = len(x)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if x[j] < x[j - 1]:
                x[j], x[j - 1] = x[j - 1], x[j]
            else:
                break
    return x