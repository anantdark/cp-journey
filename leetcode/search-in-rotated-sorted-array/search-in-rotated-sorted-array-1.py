from typing import List

# Optimal Solution - 1
# Time Complexity - O(log(n)) | Space Complexity - O(1)
# In this approach, we use binary search to find the pivot point and then check if the element could be present after or before pivot. After that another binary search to find the target element.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(i: int, j: int) -> int:
            while i <= j:
                mid = i + (j-i)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    j = mid - 1
                else:
                    i = mid + 1
            return -1
        
        # Finding inflection point/ pivot point
        if nums[0] <= nums[-1]:
            # already rotated to original position
            return binary_search(0, len(nums)-1)
        
        i, j = 0, len(nums)-1
        mid = 0
        while i <= j:
            mid = i + (j-i)//2
            if nums[mid] < nums[mid-1]:
                break
            elif nums[mid] > nums[mid+1]:
                # set mid to pivot
                mid = mid + 1
                break
            else:
                if nums[mid] > nums[i]:
                    i = mid + 1
                else:
                    j = mid - 1
        
        # check if element could be present after or before pivot
        if nums[-1] >= target:
            return binary_search(mid, len(nums)-1)
        else:
            return binary_search(0, mid)

        ##
        print(nums)


arr = [3, 1]
target = 1 
k = Solution().search(arr, target)
print(k)

# https://leetcode.com/problems/search-in-rotated-sorted-array/
