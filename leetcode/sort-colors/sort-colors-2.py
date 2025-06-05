from typing import List, Optional
from collections import defaultdict

# Naive solution
# Time O(n) | Space O(1)
# This is dutch national flag problem solution, we use three pointers two at opposite ends and md is moved from lo to hi swapping 0 with lo and 2 with hi

class Solution:
    def sortColors(self, nums: List[int]): 
        """
        Do not return anything, modify nums in-place instead.
        """
        lo, md, hi = 0, 0, len(nums)-1
        while md <= hi:
            if nums[md] == 0:
                nums[md], nums[lo] = nums[lo], nums[md]
                lo += 1
                md += 1
            elif nums[md] == 2:
                nums[md], nums[hi] = nums[hi], nums[md]
                hi -= 1
            else:
                md += 1
        return nums

## 
        print(nums)
arr = [2, 0, 1]
k = Solution().sortColors(arr)
print(k)
        
# https://leetcode.com/problems/sort-colors/
