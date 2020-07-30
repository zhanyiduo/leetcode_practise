'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return None
        else:
            for i in reversed(range(1, len(nums))):
                if nums[i - 1] >= nums[i]:
                    continue
                else:
                    for j in range(i, len(nums) - 1):
                        if nums[i - 1] < nums[j] and nums[i - 1] >= nums[j + 1]:
                            temp = nums[i - 1]
                            nums[i - 1] = nums[j]
                            nums[j] = temp
                            nums[i:] = list(reversed(nums[i:]))
                            return None
                    if nums[i - 1] < nums[len(nums) - 1]:
                        j = len(nums) - 1
                        temp = nums[i - 1]
                        nums[i - 1] = nums[j]
                        nums[j] = temp
                        nums[i:] = list(reversed(nums[i:]))
                        return None
            nums.reverse()
            return None
