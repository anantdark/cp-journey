from typing import List

# Better Solution
# We can see that for each element for which we need to find products, we can divide the array in two parts where one part is after the element and one is before, we need to compute the product of these parts. For this we can use the concept of prefix sum, In prefix sum the element at position `i` indicates the sum of all values before i, we can follow similar suit but with multiplication and create a prefix_multiplication_array and another suffix_multiplication_array.

# ex-
# a = [1, 2, 3, 4]
# prefix_multiplication_array = [1, 1, 2, 6]
# suffix_multiplication_array = [24, 12, 4, 1]

# Now you can see if we want to calculate the final value for 3, we have prefix_value for 3 is "2" and suffix_value is "4" we multiply both parts to get 12, which is the answer.
# We have essentially pre-computed the prefix and suffix multiplication values and are using them for each element.
#
# -- 
# Optimal Solution
# To optimise this further, we can solve in O(1) space {final_array is not considered as extra space by LC}
# If you notice, we are using the values only once to create the final array, so to optimize this, we can store either prefix/suffix computation in the final array and calculate the other value on the fly and update in the final array.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_length = len(nums)
        prefix_array = [1] * array_length
        suffix_array = [1] * array_length
        final_array = list()

        prefix_value = 1
        suffix_value = 1
        for i in range(len(nums)):
            prefix_array[i] = prefix_value
            prefix_value *= nums[i]
        
        for j in range(len(nums)-1, -1 , -1):
            suffix_array[j] = suffix_value
            suffix_value *= nums[j]

        for k in range(len(nums)):
            final_array.append(prefix_array[k] * suffix_array[k])
        
        return final_array
        
        
## 
        print(nums)
nums = [1, 2, 3, 4]
k = Solution().productExceptSelf(nums)
print(k)
        
# https://leetcode.com/problems/product-of-array-except-self/
