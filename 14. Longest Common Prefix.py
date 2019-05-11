'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''
class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            strs = ['']
        strs_sort = sorted(strs,key=len)
        commonprefix = ""
        for i in strs_sort[0]:
            commonprefix += i
            if all([s.startswith(commonprefix) for s in strs]):
                continue
            else:
                commonprefix = commonprefix[0:-1]
                break
        return commonprefix

testrun = Solution()
output = testrun.longestCommonPrefix(strs=[])
print(output)
