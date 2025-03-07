from typing import List

# -- Constraints
# - Modify array in-place using O(1) extra memory

# optmized solution
# Time O(n) | Space O(n) {recursion stack take use O(n)}
# Iterative approach, we use two pointers on both ends to swap and move them inwards until they meet.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

## 
        print(s)
arr = ['h', 'e', 'l', 'l', 'o']
k = Solution().reverseString(arr)
print(k)
        
# https://leetcode.com/problems/template/
