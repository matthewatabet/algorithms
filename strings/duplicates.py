#!/usr/bin/env python
'''
Remove duplicates from input string. But, maintain the ordering of
characters, and return the least lexagrpahical ordering.
To do this, store the largest index where each character is found.
Then, we can accumulate a result string by:
1) Checking if the last character in the current result can be
   found later and has a lesser value than the current character,
   if that's true we can pop the last character.
2) Add the current character
'''


class Solution(object):

    def removeDuplicateLetters(self, s):
        rindex = {c: i for i, c in enumerate(s)}
        result = ''
        for i, c in enumerate(s):
            if c not in result:
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
        return result


def main():
    solution = Solution()
    print solution.removeDuplicateLetters('bcabc') == 'abc'
    print solution.removeDuplicateLetters('cbacdcbc') == 'acdb'


if __name__ == '__main__':
    main()
