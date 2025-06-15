from typing import List
import math
from collections import defaultdict

# Brute solution
# Time O(N) | Space O(N)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        max_count = math.floor(len(nums)/3)
        counter = defaultdict(int)
        count = []
        for num in nums:
            counter[num] += 1
        
        for key in counter.keys():
            if counter[key] > max_count:
                count.append(key)
        return count

## 
        print(nums)
arr = [1, 3, 3]
# val = 9
k = Solution().majorityElement(arr)
print(k)
        
# https://leetcode.com/problems/majority-element-ii/
