'''
Write a function to find the longest common prefix string amongst
an array of strings.
'''


class Solution(object):

    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        mlength = min(map(len, strs))
        for i in range(mlength, 0, -1):
            compare = None
            found = True
            for s in strs:
                if compare is None:
                    compare = s[:i]
                elif compare != s[:i]:
                    found = False
                    break
            if found:
                return compare
        return ''


def main():
    s = Solution()
    print s.longestCommonPrefix(['abcd',
                                 'abcdef',
                                 'abcdg',
                                 'abcy'])

    print s.longestCommonPrefix([])
    print s.longestCommonPrefix(['', 'cat'])
    print s.longestCommonPrefix(['bat', 'bar', 'baz', 'batter'])


if __name__ == '__main__':
    main()
