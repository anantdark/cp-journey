from typing import List, Optional

# Brute solution
# Time O(N) | Space O(N)
# We know positive indexes will be positve in final array so we populate positive values at even index and negative values at odd index in a single pass.


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        answer = [-1 for _ in range(len(nums))]
        positive = 0
        negative = 0

        for val in nums:
            if val < 0:
                answer[2*negative+1] = val
                negative += 1
            else:
                answer[2*positive] = val
                positive += 1
        return answer

        ##
        print(nums)


arr = [3, 1, -2 - 5, 2, -4]
k = Solution().rearrangeArray(arr)
print(k)

# https://leetcode.com/problems/rearrange-array-elements-by-sign/
