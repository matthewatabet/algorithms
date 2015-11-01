class ImprovedMergeSort(object):
    '''
    Improves upon MergeSort by using insertion sort for small arrays,
    testing whether array is already in order, and avoiding copies by
    switching arguments in recursive calls.
    '''

    def __init__(self, data):
        self.data = data
        self.aux = [None] * len(data)
        self.sort(self.data)

    def __str__(self):
        return str(self.data)

    def ex(self, a, i, j):
        t = a[i]
        a[i] = a[j]
        a[j] = t

    def merge(self, a, lo, mid, hi):
        i = lo
        j = mid + 1

        if a is self.data:
            b = self.aux
        else:
            b = self.data

        for k in range(lo, hi + 1):

            # If lo end is consumed, pull from hi end.
            if i > mid:
                a[k] = b[j]
                j += 1

            # If hi end is consumed, pull from lo end.
            elif j > hi:
                a[k] = b[i]
                i += 1

            # Otherwise, pull from whichever pile has the smaller item.
            elif b[j] < b[i]:
                a[k] = b[j]
                j += 1
            else:
                a[k] = b[i]
                i += 1

    def insertion_sort(self, a, lo, hi):
        for i in range(lo, hi+1):
            for j in range(i, 0, -1):
                if a[j] > a[j-1]:
                    break
                self.ex(a, j, j-1)

    def sort(self, a, lo=None, hi=None):
        # Initialize defaults.
        if lo is None:
            lo = 0
        if hi is None:
            hi = len(a) - 1

        b = self.data
        if a is self.data:
            b = self.aux

        # Are we done?
        if hi <= lo:
            return

        if hi - lo < 10:
            self.insertion_sort(b, lo, hi)
        else:
            mid = lo + (hi - lo)/2
            self.sort(b, lo, mid)
            self.sort(b, mid+1, hi)

            # Skip merge if sub-arrays are already sorted.
            if (a[mid] is not None and
                    a[mid+1] is not None and
                    a[mid] <= a[mid+1]):
                return
            self.merge(a, lo, mid, hi)

print ImprovedMergeSort([3, 2, 6, 5, 3, 3])
print ImprovedMergeSort([7, 2, 3, 5, 5, 8, 5, 2, 4, 31, 23, 15, 22, 19, 23,
                         44, 1, 13, 12, 18, 24, 25])
