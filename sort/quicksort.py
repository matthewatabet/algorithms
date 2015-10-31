import random


def ex(data, i, j):
    t = data[i]
    data[i] = data[j]
    data[j] = t


def partition(data, lo, hi):

    p = random.randint(lo, hi)
    v = data[p]
    ex(data, p, lo)

    i = lo
    j = hi + 1

    while True:
        i += 1
        while data[i] < v:
            if i >= hi:
                break
            i += 1

        j -= 1
        while data[j] >= v:
            if j <= lo:
                break
            j -= 1

        if i >= j:
            break

        ex(data, i, j)

    ex(data, lo, j)
    return j


def quick_sort(data, lo=None, hi=None):
    if lo is None:
        lo = 0
    if hi is None:
        hi = len(data) - 1
    if lo >= hi:
        return
    j = partition(data, lo, hi)
    quick_sort(data, lo, j - 1)
    quick_sort(data, j + 1, hi)

data = [1, 3, 2]
quick_sort(data)
print data

data = [1, 5, 5, 6, 2, 8, 2]
quick_sort(data)
print data

data = [67, 34, 22, 16, 16, 22, 100, 22, 13, 15]
quick_sort(data)
print data

data = [2, 1, 1, 1]
quick_sort(data)
print data

data = [53, 22, 22, 13, 45, 22]
quick_sort(data)
print data
