class MergeSort(object):

    def __init__(self, data):
        self.data = data
        self.aux = None
        self.sort()

    def __str__(self):
        return str(self.data)

    def merge(self, lo, mid, hi):
        i = lo
        j = mid + 1

        # copy data into auxilary array for sorting.
        for k in range(lo, hi + 1):
            self.aux[k] = self.data[k]

        for k in range(lo, hi + 1):

            # If lo end is consumed, pull from hi end.
            if i > mid:
                self.data[k] = self.aux[j]
                j += 1

            # If hi end is consumed, pull from lo end.
            elif j > hi:
                self.data[k] = self.aux[i]
                i += 1

            # Otherwise, pull from whichever pile has the smaller item.
            elif self.aux[j] < self.aux[i]:
                self.data[k] = self.aux[j]
                j += 1
            else:
                self.data[k] = self.aux[i]
                i += 1

    def sort(self, lo=None, hi=None):
        # Initialize defaults.
        if lo is None:
            lo = 0
        if hi is None:
            hi = len(self.data) - 1
        if self.aux is None:
            self.aux = [None] * len(self.data)

        # Are we done?
        if hi <= lo:
            return

        mid = lo + (hi - lo)/2
        self.sort(lo, mid)
        self.sort(mid+1, hi)
        self.merge(lo, mid, hi)
        return self.data

print MergeSort([3, 2, 6, 5, 3, 3])
print MergeSort([7, 2, 3, 5, 5, 8, 5])
