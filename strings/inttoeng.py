'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
'''

ones = {'1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine'}

teens = {'10': 'Ten',
         '11': 'Eleven',
         '12': 'Twelve',
         '13': 'Thirteen',
         '14': 'Fourteen',
         '15': 'Fifteen',
         '16': 'Sixteen',
         '17': 'Seventeen',
         '18': 'Eighteen',
         '19': 'Nineteen'}

tens = {'2': 'Twenty',
        '3': 'Thirty',
        '4': 'Forty',
        '5': 'Fifty',
        '6': 'Sixty',
        '7': 'Seventy',
        '8': 'Eighty',
        '9': 'Ninety'}

denoms = {0: 'Thousand',
          1: 'Million',
          2: 'Billion',
          3: 'Trillion',
          4: 'Quadrillion'}


class Solution(object):

    def numberToWords(self, num):

        result = ''

        str_num = str(num)

        if str_num == '0':
            return 'Zero'

        i = len(str_num) - 1
        j = 0
        denom = 0
        while i >= 0:
            c = str_num[i]
            if j == 0 and c != '0':
                if i > 0 and str_num[i-1] == '1':
                    result = teens['1' + c] + ' ' + result
                    i -= 1
                else:
                    result = ones[c] + ' ' + result
            elif j == 1 and c != '0':
                result = tens[c] + ' ' + result

            elif j == 2 and c != '0':
                result = ones[c] + ' Hundred ' + result
            i -= 1
            j += 1

            if j % 3 == 0:
                j = 0
                if i >= 0 and str_num[i-2: i+1] != '000':
                    result = denoms[denom] + ' ' + result
                denom += 1

        if result.endswith(' '):
            result = result[:-1]
        return result


def main():
    s = Solution()
    print s.numberToWords(3222)
    print s.numberToWords(12345)
    print s.numberToWords(1234567)
    print s.numberToWords(500000)
    print s.numberToWords(5000000)
    print s.numberToWords(5000200)
    print s.numberToWords(923000000000000)

if __name__ == '__main__':
    main()
