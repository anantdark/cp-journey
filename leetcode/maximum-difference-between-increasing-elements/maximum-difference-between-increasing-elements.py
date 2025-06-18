from typing import List

# _ solution
# Time O() | Space O()

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        k = [nums[0]]
        for i in range(1, len(nums)):
            k.append(min(k[-1], nums[i]))
        maxdiff = -1
        for j in range(1, len(nums)):
            diff = nums[j] - k[j]
            if diff > maxdiff:
                maxdiff = diff
        return maxdiff if maxdiff > 0 else -1

## 
        print(nums)
arr = [9,4,3,2]
# val = 9
k = Solution().maximumDifference(arr)
print(k)
        
# https://leetcode.com/problems/maximum-difference-between-increasing-elements/
