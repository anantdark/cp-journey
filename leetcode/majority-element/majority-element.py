from typing import List

# Optimal solution
# Time O(N) | Space O(1)
# We are using Boyers-Moore Voting Algorithm, we are maintaining a major variable with its count, whenever we encounter the "major" value in nums while iterating we increase the count and whenever we encounter any other value we decrement by one. The logic is that since the majority element occupies more than half of the total length, even we we keep reducing count we will have atleast 1 count left to make it a >nums//2 element. So at last whatever element remains in major is the majority element. Since problem states we will always have a majority element in test cases we don't need to verify the count of major.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, count = 0, 0
        for num in nums:
            if num == major:
                count += 1
            elif count == 0:
                major = num
                count = 1
            else:
                count -= 1
        return major

## 
        print(nums)
arr = [2, 7, 11, 15]
# val = 9
k = Solution().majorityElement(arr)
print(k)
        
# https://leetcode.com/problems/majority-element/
