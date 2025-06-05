from typing import List, Optional

# Better solution
# Time O(N) | Space O(N)
# We are calling the find_next method that finds the next positive/negative number for each index.


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = -1, -1
        answer = list()

        def find_next(index, is_positive, nums=nums):
            while index < len(nums):
                index += 1
                if is_positive and nums[index] > 0:
                    return index
                elif not is_positive and nums[index] < 0:
                    return index

        for i in range(len(nums) // 2):
            positive = find_next(positive, True)
            answer.append(nums[positive])
            negative = find_next(negative, False)
            answer.append(nums[negative])
        return answer

        ##
        print(nums)


arr = [3, 1, -2 - 5, 2, -4]
k = Solution().rearrangeArray(arr)
print(k)

# https://leetcode.com/problems/rearrange-array-elements-by-sign/
