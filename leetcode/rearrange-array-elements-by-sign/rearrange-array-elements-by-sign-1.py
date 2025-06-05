from typing import List, Optional

# Brute solution
# Time O(N*2) | Space O(N)
# We are maintaining two lists with positive and negative values and inserting them alternatively in answer.
# The pop operation is O(N) as well.


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = list(), list()
        for val in nums:
            if val > 0:
                positive.append(val)
            else:
                negative.append(val)
        
        answer = list()

        while positive and negative:
            answer.append(positive.pop(0))
            answer.append(negative.pop(0))
        
        return answer

        ##
        print(nums)


arr = [3, 1, -2 - 5, 2, -4]
k = Solution().rearrangeArray(arr)
print(k)

# https://leetcode.com/problems/rearrange-array-elements-by-sign/
