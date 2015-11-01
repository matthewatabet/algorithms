import random


def ex(data, i, j):
    '''
    Exchange the items i and j within data.
    '''
    t = data[i]
    data[i] = data[j]
    data[j] = t


def partition(data, lo, hi):
    '''
    Perofrm an in-place partitioning of the list data. Selects a pivot index
    at random and then ensures that all elements between (and including) lo
    and hi are organized so values less than the pivot are on the left hand
    side of the array and those greater than the pivot are on the right hand
    side.

    Returns the pivot index.
    '''

    # Pick a random pivot. Place this value at the beginning of the array
    # so we can easily partition the rest of the array without needing to
    # track where the pivot is located.
    p = random.randint(lo, hi)
    v = data[p]
    ex(data, p, lo)

    # We start i at lo since we will immediately increment i and thus skip
    # lo. This leaves the pivot undisturbed. j begins at hi + 1 as we
    # immediately decrement j and but do want to include hi in our
    # partitioning.
    i = lo
    j = hi + 1

    while True:

        # Scan left.
        i += 1
        while data[i] < v:
            # Check bounds.
            if i >= hi:
                break
            i += 1

        # Scan right.
        # Include values which are equal to the pivot to handle duplicate
        # pivot values.
        j -= 1
        while data[j] >= v:
            # Check bounds.
            if j <= lo:
                break
            j -= 1

        # If i and j have passed each other, we're done.
        if i >= j:
            break

        # Exchange i and j, since we know both values are out of place.
        ex(data, i, j)

    # Place the pivot in its final location.
    ex(data, lo, j)
    return j


def quick_sort(data, lo=None, hi=None):
    '''
    Sort data by recursively partitioning the array in place.
    '''
    # Set defaults.
    if lo is None:
        lo = 0
    if hi is None:
        hi = len(data) - 1

    # If lo and hi have crossed each other, we're done.
    if lo >= hi:
        return

    # Partition data[lo:hi+1], get the pivot and recursively sort the rest
    # of the array.
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
