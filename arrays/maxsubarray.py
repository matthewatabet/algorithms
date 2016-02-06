#!/usr/bin/env python
'''
Find the max subarray. This works because if the current sum ever drops below 0, we know
we might as well start over in terms of accumulating our array. The head at that point
doesn't do any good.

More expensive solutions to this problem include O(N^3), where we loop over all possible
arrays, calculating the complete sum for each such subarray.

The solution below is optimal and runs in O(N).
'''

def max_subarray(items):
    max_ending_here = max_so_far = 0
    for item in items:
        max_ending_here = max(0, max_ending_here + item)
        max_so_far = max(max_so_far, max_ending_here)
        print item, max_ending_here, max_so_far
    return max_so_far


def main():
    print max_subarray([2, 1, 2, -6, -6, 7, 8])

if __name__ == '__main__':
    main()
