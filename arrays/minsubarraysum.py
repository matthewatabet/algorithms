'''
Return the shortest subarray whose sum exceeds a given threshold.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''


class Solution(object):

    def minSubArrayLen(self, s, nums):
        '''
        :type s: int
        :type nums: List[int]
        :rtype: int
        '''
        if not nums:
            return 0
        current_sum = nums[0]
        start = 0
        end = 0
        min_length = 0

        if current_sum >= s:
            min_length = 1

        while end < len(nums):
            if current_sum >= s:
                current_sum -= nums[start]
                start += 1
            else:
                end += 1
                if end == len(nums):
                    break
                current_sum += nums[end]

            if current_sum >= s:
                current_length = (end - start) + 1
                if min_length == 0 or current_length < min_length:
                    min_length = current_length

        return min_length


def main():

    s = Solution()
    assert(s.minSubArrayLen(5, [2, 4, 1, 5, 7]) == 1)
    assert(s.minSubArrayLen(20, [2, 1, 2, 2, 4]) == 0)
    assert(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2)
    assert(s.minSubArrayLen(6, [10, 2, 3]) == 1)

if __name__ == '__main__':
    main()
