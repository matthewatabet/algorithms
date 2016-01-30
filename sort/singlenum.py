#!/usr/bin/env python
'''
Given an array of integers where all numbers but one occur three times, find
the single number which occurs just once.
'''


class Solution(object):

    def singleNumber(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        counts = {}
        for n in nums:
            counts.setdefault(n, 0)
            counts[n] += 1
        for n, count in counts.items():
            if count != 3:
                return n


def main():
    s = Solution()
    assert(s.singleNumber([4, 5, 5, 4, 4]) == 5)
    assert(s.singleNumber([5, 5, 5, 6, 6, 7, 6]) == 7)
    assert(s.singleNumber([3, 2, 3, 2, 3, 2, 2]) == 2)

if __name__ == '__main__':
    main()
