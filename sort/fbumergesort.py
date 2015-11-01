class FastBottomUpMergeSort(object):
    '''
    Efficiently handle small merges by combining them together.
    Extend bumergesort by coping the second half of each aux array
    in reversed order. This means we don't have to do bounds checking.
    '''
    def __init__(self, data):
        self.data = data
        self.aux = [None] * len(self.data)
        self.sort()

    def __str__(self):
        return str(self.data)

    def merge(self, lo, mid, hi):

        i = lo
        j = hi

        # Copy data into aux array.
        for k in range(lo, mid + 1):
            self.aux[k] = self.data[k]
        for k in range(mid + 1, hi + 1):
            self.aux[k] = self.data[hi-k+mid+1]

        # Perform merge.
        for k in range(lo, hi + 1):
            if self.aux[j] < self.aux[i]:
                self.data[k] = self.aux[j]
                j -= 1
            else:
                self.data[k] = self.aux[i]
                i += 1

    def sort(self):

        sz = 1
        while sz < len(self.data):
            lo = 0
            while lo < len(self.data) - sz:
                self.merge(lo, lo+sz-1, min(lo+sz+sz-1, len(self.data) - 1))
                lo += 2*sz
            sz *= 2

print FastBottomUpMergeSort([5, 2, 3, 2, 3, 5])
print FastBottomUpMergeSort([9, 2, 13, 1, 1, 10])
print FastBottomUpMergeSort([7, 2, 3, 1, 5, 7, 4])
