from typing import List

# -- Constraints
# - Don't use extra space, trim off extra elements after insertion

# Brute Solution (using insert)
# Time O(n^2) | Space O(N) (insert operation takes 0(n) since existing elements need to be shifted rightwards)
# We keep inserting the elements from the back and then trim at the end.

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        final_length = len(arr)
        length = final_length - 1
        while length >= 0:
            if arr[length] == 0:
                arr.insert(length, 0)
            length -= 1
        arr[:] = arr[:final_length]
        arr[:] = arr[:final_length]

## 
        print(arr)
arr = [0,4,1,0,0,8,0,0,3]
k = Solution().duplicateZeros(arr)
print(k)
        
# https://leetcode.com/problems/duplicate-zeros/
