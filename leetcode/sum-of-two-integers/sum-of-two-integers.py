from typing import List

# optimized solution
# Time O(1) | Space O(1)
# https://www.youtube.com/watch?v=MmIx_NrCkGI

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while (mask & b) > 0:
            a, b = (a ^ b), (a & b )<< 1
        return (mask & a) if b > 0 else a

## 
        print(nums)
a, b = 1, 2
k = Solution().getSum(a,b)
print(k)
        
# https://leetcode.com/problems/sum-of-two-integers/
