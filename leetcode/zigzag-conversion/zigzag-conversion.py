from typing import List

# Optimal solution
# Time O(n) | Space O(n)
# 

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        s_list = list(s)
        bar_distance = (numRows-1)*2
        levels = numRows - 2
        final_string = ""
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                final_string += "".join(s_list[i::bar_distance])
            else:
                j = i
                temp_string = ""
                mid_index = numRows - 1 + levels
                while j < len(s_list):
                    temp_string += s_list[j]
                    if mid_index < len(s_list):
                        temp_string += s_list[mid_index]
                    j += bar_distance
                    mid_index += bar_distance
                final_string += temp_string
                levels -= 1
        return final_string


## 
        # print(nums)
s = "PAYPALISHIRING"
val = 3
k = Solution().convert(s, val)
print(k)
        
# https://leetcode.com/problems/zigzag-conversion/
