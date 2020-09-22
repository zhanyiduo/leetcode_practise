'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        sol_dict = {}
        for ele in strs:
            sort_ele = ''.join(sorted(ele))
            if sort_ele not in sol_dict.keys():
                sol_dict[sort_ele] = [ele]
            else:
                sol_dict[sort_ele].append(ele)
        for key,val in sol_dict.items():
            res.append(val)
        return res