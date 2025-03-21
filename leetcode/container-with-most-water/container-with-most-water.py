from typing import List

# Optmized solution
# Time O(n) | Space O(n)
# The area for container will be dependant on the shorter line and the distance between lines, we can start from opposite ends maintaining the max area and keep moving the pointer with the shorter line. Moving the smaller line pointer can be helpful in increasing area even though the distance is decreasing.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        max_area = 0
        calculate_area = lambda i, j: (j-i) * min(height[i] , height[j])
        while i < j:
            current_area = calculate_area(i, j)
            if current_area > max_area:
                max_area = current_area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

## 
        print(nums)
arr = [1,8,6,2,5,4,8,3,7]
k = Solution().maxArea(arr)
print(k)
        
# https://leetcode.com/problems/container-with-most-water/
