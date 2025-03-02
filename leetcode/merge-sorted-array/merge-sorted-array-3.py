from typing import List

# Better solution
# Time O(n+m) | Space O(1)
# In this problem, instead of copying arr1, we can traverse both arrays in reverse and insert from the back as it is already 0 so we won't override any value.


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        for p in range(n+m-1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1


        ##
        print(nums1)


arr1 = [2, 0]
arr2 = [1]
m = 1
n = 1
k = Solution().merge(arr1, m, arr2, n)
print(k)

# https://leetcode.com/problems/merge-sorted-array/
