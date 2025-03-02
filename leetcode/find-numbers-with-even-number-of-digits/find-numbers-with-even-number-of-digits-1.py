from typing import List

# Better solution
# Time O(n * m) | Space O(n) (m is the number of digits in the integer)
# In this problem, we convert each number to string and calculate it's length, if it is even we increment the counter. Converting to string and calculating length requires O(m) time.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0
        for num in nums:
            length = len(str(num))
            if length%2==0:
                even_count += 1
        return even_count

## 
        print(nums)
arr = [12,345,2,6,7896]
k = Solution().findNumbers(arr)
print(k)
        
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
