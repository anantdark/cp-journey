from typing import List

# Optimal Solution - 2
# Time Complexity - O(log(n)) | Space Complexity - O(1)
# In this approach, rather than finding the pivot like earlier, we instead divide the array at mid, every time one section will be sorted, we just have to check the limits of this sorted section to see if the target is between these limits, if yes then we continue on this section otherwise move pointer to other section, repeat until we are down to one element or i becomes > j.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        mid = 0
        while i <= j:
            mid = i + (j-i)//2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] >= nums[i]:
                    if target < nums[mid] and target >= nums[i]:
                        j = mid - 1
                    else:
                        i = mid + 1
                else:
                    if target <= nums[j] and target > nums[mid]:
                        i = mid + 1
                    else:
                        j = mid -1
        return -1
        
        ##
        print(nums)


arr = [3, 1]
target = 1 
k = Solution().search(arr, target)
print(k)

# https://leetcode.com/problems/search-in-rotated-sorted-array/
