'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
def twoSum(nums, target):
    for i in nums:
        if (target - i) in nums:
            ix = nums.index(i)
            ix2 = nums.index(target - i)
            if ix != ix2:
                return [ix, ix2]
            else:
                nums_copy = nums.copy()
                nums_copy.remove(i)
                if (target - i) in nums_copy:
                    ix2 = nums_copy.index(target - i)+1
                    return [ix, ix2]
if __name__ == '__main__':
    output = twoSum(nums=[3,2,4],target=6)
    print('Output: '+ str(output))
