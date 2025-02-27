from typing import List

# Optimal Solution (TLE)
# Time Complexity: O(n) | Space Complexity: O(n)
# In this appproach, we use a dictionary to store the number we have encountered, if it is already present we can be sure of duplicates.
# Note: We can also use a set here


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict: dict = {}
        for i in nums:
            if num_dict.get(i):
                return True
            else:
                num_dict[i] = True
        return False

        ##
        print(nums)


arr = [2, 7, 11, 15]
val = 9
k = Solution().containsDuplicate(arr)
print(k)

# https://leetcode.com/problems/contains-duplicate/
