from typing import List

# _ solution
# Time O() | Space O()

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        counter = 0
        current = 0
        prev = current
        while i < len(nums):
            current = nums[i]
            if prev != current:
                counter = 0
                prev = current
            counter += 1
            nums[i], nums[j] = nums[j], nums[i]
            if counter <= 2:
                i += 1
                j += 1
            else:
                i += 1
        return j

        

## 
        print(nums)
arr = [1,1,1,2,2,3]
# val = 5
k = Solution().removeDuplicates(arr)
print(k)
        
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
