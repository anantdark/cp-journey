from typing import List
import math
from collections import defaultdict

# Optimal solution
# Time O(N) | Space O(1)
# We are using Boyer-Moore Voting Algorithm. If we have to print numbers with more than n/3 occurences we can have atmost 2 possible values mathematically. So we will maintain two values(val1, val2) with their counts(count1, count2). When we iterate the array, we keep incrementing the counter if the value is encountered, and decrement the counter if any other value is encountered till counter is greater than 0, if counter reaches 0 we replace the value with current value of num. After the traversal we will get two possible solutions, but we will have to get their count to verify because if the array has no value with >n/3 occurences still val1, val2 will hold some value. So two passes will still be required to get the count of these two possible solutions. But overall the TC will remain as O(N). And since we are not using extra space other than some variables, the SC is O(1).

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2, val1, val2 = 0, 0, 0, 1
        for num in nums:
            if num == val1:
                count1 += 1
            elif num == val2:
                count2 += 1
            elif count1 == 0:
                val1 = num
                count1 = 1
            elif count2 == 0:
                val2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        return [n for n in (val1, val2) if nums.count(n)>(len(nums)//3)]

## 
        print(nums)
arr = [1, 3, 3]
# val = 9
k = Solution().majorityElement(arr)
print(k)
        
# https://leetcode.com/problems/majority-element-ii/
