from typing import List

# -- Constraints
# - Don't use extra space, trim off extra elements after insertion

# Initial Solution (using insert) {Incorrect}
# Time O(n) | Space O(1)
# We need to loop two times, once from the front to count the number of zeroes and till the index after which array will go outside original length. Then loop back from that index overriding the elements from -1 index and adding extra zeroes.


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr_length = len(arr)
        i = 0
        while arr_length > 0 and i < len(arr):
            if arr[i] == 0:
                arr_length -= 2
            else:
                arr_length -= 1
            i += 1
        j = len(arr)-1
        i -= 1
        if arr_length < 0:
            arr[-1] = 0
            j -= 1
            i -= 1
        while j >= 0:
            if arr[i] == 0:
                arr[j] = 0
                arr[j-1] = 0
                j -= 2
            else:
                arr[j] =  arr[i]
                j -= 1
            i -= 1
            

## 
        print(arr)
arr = [1, 2, 3]
k = Solution().duplicateZeros(arr)
print(k)
        
# https://leetcode.com/problems/duplicate-zeros/
