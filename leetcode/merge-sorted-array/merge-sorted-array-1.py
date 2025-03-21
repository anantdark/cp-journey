from typing import List

# Naive solution
# Time O((n+m)log(n+m)) | Space O(1)
# In this problem, we can update the zeroes in num1 with elements from num2 and then sort the array.


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m + n):
            nums1[i] = nums2[i - m - 1]
        nums1.sort()

        ##
        print(arr1)


arr1 = [1, 2, 4, 5, 6, 0]
arr2 = [3]
m = 5
n = 1
k = Solution().merge(arr1, m, arr2, n)
print(k)

# https://leetcode.com/problems/merge-sorted-array/
