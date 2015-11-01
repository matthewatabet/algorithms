class BottomUpMergeSort(object):
    '''
    Efficiently handle small merges by combining them together.
    '''
    def __init__(self, data):
        self.data = data
        self.aux = [None] * len(self.data)
        self.sort()

    def __str__(self):
        return str(self.data)

    def merge(self, lo, mid, hi):

        i = lo
        j = mid + 1

        # Copy data into aux array.
        for k in range(lo, hi + 1):
            self.aux[k] = self.data[k]

        # Perform merge.
        for k in range(lo, hi + 1):

            # Pull from hi end if lo end is consumed.
            if i > mid:
                self.data[k] = self.aux[j]
                j += 1
            # Pull from lo end if hi end is consumed.
            elif j > hi:
                self.data[k] = self.aux[i]
                i += 1
            # Pull from whichever pile has the next lowest element.
            elif self.aux[i] < self.aux[j]:
                self.data[k] = self.aux[i]
                i += 1
            else:
                self.data[k] = self.aux[j]
                j += 1

    def sort(self):

        sz = 1
        while sz < len(self.data):
            lo = 0
            while lo < len(self.data) - sz:
                self.merge(lo, lo+sz-1, min(lo+sz+sz-1, len(self.data) - 1))
                lo += 2*sz
            sz *= 2

print BottomUpMergeSort([5, 2, 3, 2, 3, 5])
print BottomUpMergeSort([9, 2, 13, 1, 1, 10])
