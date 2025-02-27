from typing import List

# Optmized solution
# Time O(n) | Space O(n)
# In this problem, we can use a dictionary to store the number and its index. If the target - number is in the dictionary, we can return the index of the number and the index of the target - number. Because each array can only contain a single solution.

class Solution:
    def twoSum(self, nums: List[int], target: int):
        sum_dict = dict()
        for i in range(len(nums)):
            other_number = target - nums[i]
            if sum_dict.get(other_number) is not None:
                return [i, sum_dict[other_number]]
            else:
                sum_dict[nums[i]] = i

## 
        print(nums)
arr = [2, 7, 11, 15]
val = 9
k = Solution().twoSum(arr, val)
print(k)
        
# https://leetcode.com/problems/two-sum/
