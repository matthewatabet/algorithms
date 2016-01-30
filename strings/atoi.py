#!/usr/bin/env python
'''
Convert a string to an integer.
'''
INT_MAX = 2147483647
INT_MIN = -2147483648

DIGITS = {'0': 0,
          '1': 1,
          '2': 2,
          '3': 3,
          '4': 4,
          '5': 5,
          '6': 6,
          '7': 7,
          '8': 8,
          '9': 9}


class Solution(object):

    def myAtoi(self, s):
        '''
        :type str: str
        :rtype: int
        '''
        s = s.strip()
        neg = False
        x = 0

        if not s:
            return x

        i = 0
        if s[i] == '-':
            neg = True
            i += 1
        elif s[i] == '+':
            i += 1

        while i < len(s):
            if s[i] in DIGITS:
                x *= 10
                x += DIGITS[s[i]]
                i += 1
            else:
                break
        if neg:
            return max(-x, INT_MIN)
        else:
            return min(x, INT_MAX)


def main():
    s = Solution()
    assert(s.myAtoi('   45') == 45)
    assert(s.myAtoi('589') == 589)
    assert(s.myAtoi('-13') == -13)
    assert(s.myAtoi('xx') == 0)
    assert(s.myAtoi('23jj') == 23)
    assert(s.myAtoi('0') == 0)
    assert(s.myAtoi('  -45') == -45)

if __name__ == '__main__':
    main()
