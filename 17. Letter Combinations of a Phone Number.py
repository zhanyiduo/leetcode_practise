'''iven a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # create a digit to str lookup
        digitlookup = {}
        i = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for key in range(2, 10, 1):
            if key not in [7, 9]:
                digitlookup[str(key)] = [x for x in alphabet[i:i + 3]]
                i += 3
            else:
                digitlookup[str(key)] = [x for x in alphabet[i:i + 4]]
                i += 4
        # using dynamic programming
        dp = []
        if not digits:
            return []
        dp.append(digitlookup[digits[0]])
        for idx, digit in enumerate(digits[1:]):
            string = digitlookup[digit]
            dp.append([k + j for k in dp[-1] for j in string])

        return dp[-1]