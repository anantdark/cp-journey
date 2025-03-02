from typing import List

# Better solution
# Time O(n+m) | Space O(n)
# In this problem, we are copying nums1 elements to a new array then using pointers on both array to merge in final array.


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr1 = nums1[:m]
        i, j = 0, 0
        k = 0
        while i < len(arr1) and j < len(nums2):
            if arr1[i] < nums2[j]:
                nums1[k] = arr1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

        while i < len(arr1):
            nums1[k] = arr1[i]
            i += 1
            k += 1
        while j < len(nums2):
            nums1[k] = nums2[j]
            j += 1
            k += 1


        ##
        print(nums1)


arr1 = [1,2,3,0,0,0]
arr2 = [2,5, 6]
m = 3
n = 3
k = Solution().merge(arr1, m, arr2, n)
print(k)

# https://leetcode.com/problems/merge-sorted-array/
