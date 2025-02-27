from typing import List

class Solution:
    def longestSubarray(self, arr, k):  
        i = 0
        j = len(arr) - 1
        current_sum = sum(arr[i:j+1])
        while i < j or current_sum > k:
            if current_sum == k:
                return j - i + 1
            if arr[i] < arr[j]:
                current_sum -= arr[i]
                i += 1
            else:
                current_sum -= arr[j]
                j -= 1
        return 0




## 
        # print(nums)
arr = [1, 2, 3, 10, 5, 2, 7, 1, 0, 0, -10, 2]
k = 15
ak = Solution().longestSubarray(arr, k)
print(ak)
        
# https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1
