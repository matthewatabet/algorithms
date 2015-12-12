'''
Given an array of integers, find two numbers such that they add up 
to a specific target number.

The function twoSum should return indices of the two numbers such that
they add up to the target, where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are not
zero-based.

You may assume that each input would have exactly one solution.
'''


class Solution(object):

    def twoSum(self, nums, target):
        indices = {}
        for i, n in enumerate(nums):
            indices.setdefault(n, []).append(i)

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices:
                for j in indices[diff]:
                    if j <= i:
                        continue
                    return [i + 1, j + 1]


def main():
    s = Solution()
    print s.twoSum([2, 7, 11, 15], 9)
    print s.twoSum([6, 3, 8, 2, 1], 5)
    print s.twoSum([5, 3, 0, 6, 7, 0], 0)

if __name__ == '__main__':
    main()
