class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        elif (len(s)%2) | (not any([x in s for x in {'()','[]','{}'}])):
            return False
        else:
            for i in {'()','[]','{}'}:
                if not s:
                    return True
                elif i in s:
                    s = s.replace(i,"")
            if self.isValid(s):
                return True
            else:
                return False

testrun = Solution()
output = testrun.isValid(s='([)]')
print(output)

#output = testrun.isValid(s='[(){()}]')
print(output)

output = testrun.isValid(s='()[]{}')
print(output)