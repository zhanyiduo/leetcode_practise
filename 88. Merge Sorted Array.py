'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1[:m].copy()
        j =0
        k=0
        if m and n:
            for i in range(m+n):
                if nums3[j]<=nums2[k]:
                    nums1[i] = nums3[j]
                    j += 1
                    if j>=m:
                        nums1[i+1:] = nums2[k:]
                        break
                else:
                    nums1[i] = nums2[k]
                    k += 1
                    if k>=n:
                        nums1[i+1:] = nums3[j:]
                        break
        else:
            nums3.extend(nums2)
            nums1 = nums3