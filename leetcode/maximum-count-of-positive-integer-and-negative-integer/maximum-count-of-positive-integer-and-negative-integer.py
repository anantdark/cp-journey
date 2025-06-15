from typing import List

# Optimized solution
# Time O(logN) | Space O(1)

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1
        if len(nums) == 1:
            return 1
        elif nums[0] > 0 or nums[-1] < 0:
            return len(nums)
        elif nums[-1] == 0 and nums[0] == 0:
            return 0
        negative, positive = -1, -1
        while lo < hi:
            mid = (hi+lo)//2
            if nums[mid] < 0 and nums[mid+1] >=0:
                negative = mid+1
                break
            elif nums[mid] >= 0:
                hi = mid
            else:
                lo = mid+1
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            mid = (hi+lo)//2
            if nums[mid] > 0 and nums[mid-1] <= 0:
                positive = len(nums)-mid
                break
            elif nums[mid] <= 0:
                lo = mid + 1
            else:
                hi = mid
        
        return max(negative, positive)

## 
        print(nums)
arr = [0]
val = 9
k = Solution().maximumCount(arr)
print(k)
        
# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/
