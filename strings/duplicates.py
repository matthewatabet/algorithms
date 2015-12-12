#!/usr/bin/env python


class Solution(object):

    def removeDuplicateLetters(self, s):
        t = set([])
        for c in s:
            t.add(c)
        t = list(t)
        t.sort()
        return t


def main():
    solution = Solution()
    print solution.removeDuplicateLetters('gfvbbf')
    print solution.removeDuplicateLetters('bcabc')
    print solution.removeDuplicateLetters('acdb')


if __name__ == '__main__':
    main()
