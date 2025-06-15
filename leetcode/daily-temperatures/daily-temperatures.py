from typing import List, Optional

# Optimized solution
# Time O(n) | Space O(n)
# We use a monotonically decreasing stack to store all index with no greater element found yet, when a greater element is found we keep popping elements lower than the current element.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                ind = stack.pop()
                answer[ind] = i-ind
            stack.append(i)
        return answer

## 
        print(nums)
arr = [73, 74, 75, 71, 69, 72, 76, 73]
k = Solution().dailyTemperatures(arr)
print(k)
        
# https://leetcode.com/problems/daily-temperatures/
