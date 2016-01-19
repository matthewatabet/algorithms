'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
'''


class Solution(object):

    def findRepeatedDnaSequences(self, s):
        substrings = {}

        for i in range(0, len(s) - 9):
            substring = s[i:i+10]
            substrings.setdefault(substring, 0)
            substrings[substring] += 1

        repeated_strings = []
        for substring, count in substrings.items():
            if count == 1:
                continue
            repeated_strings.append(substring)
        return repeated_strings


def main():
    s = Solution()
    r = s.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
    assert(r == ["AAAAACCCCC", "CCCCCAAAAA"])

    r = s.findRepeatedDnaSequences('AAAAAAAAAAA')
    print r
    assert(r == ['AAAAAAAAAA'])

if __name__ == '__main__':
    main()
