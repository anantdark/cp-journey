from typing import List, Optional

# optmized solution
# Time O(num_rows^2) | Space O(1)
# 

class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        row_sum = [[1]]
        if num_rows == 1:
            return row_sum
        for i in range(1, num_rows):
            arr = [1]*(i+1)
            for j in range(1, len(arr)-1):
                arr[j] = row_sum[i-1][j] + row_sum[i-1][j-1]
            row_sum.append(arr)
        return row_sum

## 
        print(nums)
arr = 5
k = Solution().generate(arr)
print(k)
        
# https://leetcode.com/problems/pascals-triangle/
