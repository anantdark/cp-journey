from typing import List, Optional

# Optmized solution (Iterative)
# Time O(logn) | Space O(1)
#


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
        temp = 0
        n = abs(n)
        while n > 1:
            if n % 2 != 0:
                if not temp:
                    temp = x
                else:
                    temp = temp * x
                n -= 1
            x = x * x
            n = n / 2
        if temp:
            x *= temp
        return x

        ##
        print(nums)


x = 2
n = 10
k = Solution().myPow(x, n)
print(k)

# https://leetcode.com/problems/template/
