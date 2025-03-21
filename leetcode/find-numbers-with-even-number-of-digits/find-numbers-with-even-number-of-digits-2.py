from typing import List
import math

# Better solution
# Time O(n) | Space O(n) (m is the number of digits in the integer)
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/editorial/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0
        for num in nums:
            digit_count = int(math.floor(math.log10(num)))+1
            if digit_count % 2 == 0:
                even_count += 1
        return even_count


## 
        print(nums)
arr = [12,345,2,6,7896]
k = Solution().findNumbers(arr)
print(k)
        
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
