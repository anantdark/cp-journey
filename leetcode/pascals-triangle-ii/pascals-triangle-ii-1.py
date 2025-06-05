from typing import List, Optional

# Naive solution
# Time O(num_rows^2) | Space O(1)
# 

class Solution:
    def getRow(self, row_index: int) -> List[int]:
        row_sum = [1]
        prev_sum = []
        if row_index == 0:
            return row_sum
        for i in range(1, row_index+1):
            prev_sum = row_sum
            row_sum = [1]*(i+1)
            for j in range(1, len(row_sum)-1):
                row_sum[j] = prev_sum[j] + prev_sum[j-1]
        return row_sum

## 
        print(nums)
arr = 5
k = Solution().getRow(arr)
print(k)
        
# https://leetcode.com/problems/pascals-triangle-ii/
