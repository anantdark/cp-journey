from typing import List, Optional

# optmized solution (Recursive)
# Time O(num_rows^2) | Space O(1)
# 

class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        if num_rows == 1:
            return [[1]]

        prev_rows = self.generate(num_rows-1)
        new_row = [1] * num_rows

        for i in range(1, num_rows-1):
            new_row[i] = prev_rows[-1][i-1] + prev_rows[-1][i]
        prev_rows.append(new_row)
        return prev_rows

## 
        print(nums)
arr = 5
k = Solution().generate(arr)
print(k)
        
# https://leetcode.com/problems/pascals-triangle/
