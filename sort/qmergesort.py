def merge(a, b):
    '''
    Merges two sorted queues.
    '''
    c = []
    i = 0
    j = 0

    for k in range(0, len(a) + len(b)):
        if i >= len(a):
            c.append(b[j])
            j += 1

        elif j >= len(b):
            c.append(a[i])
            i += 1

        elif a[i] < b[j]:
            c.append(a[i])
            i += 1

        else:
            c.append(b[j])
            j += 1

    return c


def qsort(data):
    queues = [[d] for d in data]
    while len(queues) > 1:
        a = queues.pop(0)
        b = queues.pop(0)
        queues.append(merge(a, b))
    return queues[0]

print merge([3, 6, 8], [1, 2, 7])
print merge([5, 5, 6, 9, 10], [4, 5, 8, 8, 9])
print qsort([6, 2, 2, 3, 7, 1, 2, 9, 10])
print qsort([2, 5, 1, 1, 5, 2, 2, 3, 5, 8, 11])
