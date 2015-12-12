'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''


class Solution(object):

    def count(self, s):
        result = ''
        current = None
        count = 0
        for c in s:
            if current is None:
                current = c
                count = 1
            elif c != current:
                result += str(count) + current
                count = 1
                current = c
            else:
                count += 1
        result += str(count) + current
        return result

    def countAndSay(self, n):
        if n <= 1:
            return '1'
        else:
            return self.count(self.countAndSay(n-1))


def main():
    s = Solution()
    for i in range(1, 6):
        print s.countAndSay(i)


if __name__ == '__main__':
    main()
