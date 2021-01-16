'''
Convert a non-negative integer num to its English words representation.



Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"


Constraints:

0 <= num <= 231 - 1
'''


class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return 'Zero'
        else:
            hundreds = num % 1000
            num = int(num / 1000)
            thousands = num % 1000
            num = int(num / 1000)
            millions = num % 1000
            num = int(num / 1000)
            billions = num % 1000
            eng_billions, eng_millions, eng_thousands, eng_hundreds = '', '', '', ''
            if hundreds:
                eng_hundreds = self.underthousand(hundreds)
            if thousands:
                eng_thousands = self.underthousand(thousands) + ' Thousand '
            if millions:
                eng_millions = self.underthousand(millions) + ' Million '
            if billions:
                eng_billions = self.underthousand(billions) + ' Billion '

            res = eng_billions + eng_millions + eng_thousands + eng_hundreds
            return res[:-1] if res.endswith(' ') else res

    def underthousand(self, num):
        res = ''
        lookup = {20: "Twenty",
                  30: 'Thirty',
                  40: 'Forty',
                  50: 'Fifty',
                  60: 'Sixty',
                  70: "Seventy",
                  80: 'Eighty',
                  90: 'Ninety',
                  10: 'Ten',
                  11: 'Eleven',
                  12: 'Twelve',
                  13: 'Thirteen',
                  14: 'Fourteen',
                  15: 'Fifteen',
                  16: 'Sixteen',
                  17: 'Seventeen',
                  18: 'Eighteen',
                  19: 'Nineteen',
                  0: '',
                  1: 'One',
                  2: 'Two',
                  3: 'Three',
                  4: 'Four',
                  5: 'Five',
                  6: 'Six',
                  7: "Seven",
                  8: 'Eight',
                  9: 'Nine'}

        lesshundred = num % 100
        hundred = int(num / 100)

        eng_hundred, eng_tens, eng_single = '', '', ''
        if hundred:
            eng_hundred = lookup[hundred] + ' Hundred '
        if lesshundred >= 20:
            single = lesshundred % 10
            tens = int(lesshundred / 10) * 10
            eng_tens = lookup[tens]
            if single:
                eng_single = ' ' + lookup[single]
        else:
            eng_single = lookup[lesshundred]
        res = eng_hundred + eng_tens + eng_single
        return res[:-1] if res.endswith(' ') else res



