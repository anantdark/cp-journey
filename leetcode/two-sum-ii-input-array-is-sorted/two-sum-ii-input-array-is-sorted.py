from typing import List, Optional

# Optimized solution
# Time O(n) | Space O(1)
# We use two pointers to move from both ends, if the sum is greater than target we move right pointer inwards otherwise vice-versa.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1, ptr2 = 0, len(numbers)-1
        while ptr1 < ptr2:
            num1 = numbers[ptr1]
            num2 = numbers[ptr2]
            if (num1+num2) == target:
                return [ptr1+1, ptr2+1]
            else:
                if num1+num2 > target:
                    ptr2 -= 1
                else:
                    ptr1 += 1
        return [ptr1+1, ptr2+1]

## 
        # print(nums)
arr = [2, 7, 11, 15]
target = 9
k = Solution().twoSum(arr, target)
print(k)
        
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
