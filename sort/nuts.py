def ex(data, i, j):
    print '%s<=>%s %s' % (i, j, data)
    t = data[i]
    data[i] = data[j]
    data[j] = t
    print '==', data


def partition(data, v, lo, hi):

    j = lo
    if data[lo] == v:
        ex(data, lo, hi)
    for i in range(lo, hi):
        print 'v=%s i=%s data[i]=%s lo=%s hi=%s' % (v, i, data[i], lo, hi)
        if data[i] < v:
            print 'swap'
            ex(data, i, j)
            j += 1
        if data[i + 1] == v:
            print 'pivot in', i + 1, hi
            ex(data, i + 1, hi)
    pivot = hi
    if data[hi] < data[j]:
        print 'pivot out'
        ex(data, hi, j)
        pivot = j
    print data[:j], data[j], data[j+1:]
    print ''
    return pivot


# partition([5, 2, 3, 3, 5], 3, 0, 4)
# partition([1, 1, 1, 2, 1], 1, 0, 4)
# partition([9, 3, 8, 2, 1], 2, 0, 4)
partition([7, 9, 2, 5, 4, 3], 7, 0, 5)


def nuts_and_bolts(nuts, bolts, lo=None, hi=None):
    if lo is None:
        lo = 0
    if hi is None:
        hi = len(nuts) - 1

    if lo >= hi:
        return

    v = nuts[lo]
    j = partition(nuts, v, lo, hi)
    partition(bolts, v, lo, hi)

    nuts_and_bolts(nuts, bolts, lo, j - 1)
    nuts_and_bolts(nuts, bolts, j + 1, hi)


nuts = [1, 5, 0]
bolts = [5, 1, 0]
nuts_and_bolts(nuts, bolts)
print nuts, bolts

nuts = [7, 9, 2, 5, 4, 3]
bolts = [5, 3, 9, 7, 4, 2]
nuts_and_bolts(nuts, bolts)
print nuts, bolts
