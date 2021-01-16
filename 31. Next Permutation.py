'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''
#https://www.cnblogs.com/grandyang/p/4428207.html
'''
solution:
1. find the first desending item from backwards.record the index as i
2. find the first item greater than nums[i], record the index as j
3. swap nums[i] and nums[j]
4. reverse nums[i+1:]
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                for j in range(n - 1, i, -1):
                    if nums[j] > nums[i]:
                        break
                nums[i], nums[j] = nums[j], nums[i]
                nums[i + 1:] = nums[i + 1:][::-1]
                return
        nums.reverse()
