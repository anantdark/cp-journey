from typing import List

# Brute Solution (MLE)
# Time complexity: O(n^3) | Space complexity: O(n^2)
# In in Brute solution we are traversing all the subarrays and summing them, then returning the maximum sum.


class Solution:
    @staticmethod
    def generate_subarray(arr: list):
        subarray_list: list = list()
        for i in range(len(arr)):
            for j in range(i+1, len(arr)+1):
                subarray_list.append(arr[i:j])
        return subarray_list

    def maxSubArray(self, nums: List[int]) -> int:
        subarrays = self.generate_subarray(nums)
        max_sum = int(-1e5)
        for arr in subarrays:
            summation = sum(arr)
            if summation >= max_sum:
                max_sum = summation
        return max_sum


        ##
        print(nums)


arr = [5, 4, -1, 7, 8]
k = Solution().maxSubArray(arr)
print(k)

# https://leetcode.com/problems/maximum-subarray/
