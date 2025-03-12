from typing import List

class Solution:
    def reverseArray(self, arr):
        def reverse(arr, start, end):
            if start >= end:
                return arr
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
            return reverse(arr, start, end)
        return reverse(arr, 0, len(arr)-1)



## 
        print(arr)
arr = [1, 4, 3, 2, 6, 5]
ak = Solution().reverseArray(arr)
print(ak)
        
# https://www.geeksforgeeks.org/problems/reverse-an-array/0
