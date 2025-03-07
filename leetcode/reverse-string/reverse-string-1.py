from typing import List

# -- Constraints
# - Modify array in-place using O(1) extra memory

# better solution
# Time O(n) | Space O(n) {recursion stack take use O(n)}
# Recursive approach, we swap the edges and call method again with both sides reduced by 1 element until i meets j.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left+1, right-1)
        helper(0, len(s)-1)

## 
        print(s)
arr = ['h', 'e', 'l', 'l', 'o']
k = Solution().reverseString(arr)
print(k)
        
# https://leetcode.com/problems/template/
