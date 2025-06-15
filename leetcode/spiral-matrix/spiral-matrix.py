from typing import List

# Optimal solution
# Time O(N) | Space O(N)
# We have to maintain 4 pointers(start_height, end_height, start_width, end_width) and simulate the movement of pointer across the matrix spirally.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def check_valid(i, j, start_height, end_height, start_width, end_width):
            return i >= start_height and i < end_height and j >= start_width and j < end_width
        end_width = len(matrix[0])
        end_height = len(matrix)
        start_height, start_width = 0, 0
        i, j = 0, 0
        answer = list()
        while end_width - start_width:
            if not check_valid(i, j, start_height, end_height, start_width, end_width):
                break
            while j < end_width:
                answer.append(matrix[i][j])
                j += 1
            start_height += 1
            j = end_width - 1
            i += 1
            if check_valid(i, j, start_height, end_height, start_width, end_width):
                while i < end_height:
                    answer.append(matrix[i][j])
                    i += 1
                end_width -= 1
                i = end_height - 1
                j -= 1
            if check_valid(i, j, start_height, end_height, start_width, end_width):
                while j >= start_width:
                    answer.append(matrix[i][j])
                    j -= 1
                end_height -= 1
                j = start_width
                i -= 1
            if check_valid(i, j, start_height, end_height, start_width, end_width):
                while i >= start_height:
                    answer.append(matrix[i][j])
                    i -= 1
                start_width += 1
                j += 1
                i = start_height
        return answer

## 
        # print(nums)
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
val = 9
k = Solution().spiralOrder(arr)
print(k)
        
# https://leetcode.com/problems/spiral-matrix/
