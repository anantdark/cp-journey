from typing import List

# _ solution
# Time O() | Space O()

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        arr = list()
        flag = False
        lb = 0
        hb = 0
        for i in range(len(intervals)-1):
            if i == len(intervals)-1:
                if flag:
                    arr.append([lb, hb])
                    return arr
                else:
                    arr.append(intervals[i])
            else:
                if intervals[i][1] >= intervals[i+1][0]:
                    if not flag:
                        lb = intervals[i][0]
                        hb = intervals[i+1][1]
                        flag = True
                    else:
                        hb = intervals[i+1][1]
                else:
                    if flag:
                        flag = False
                        arr.append([lb, hb])
                    else:
                        arr.append(intervals[i])
        return arr

## 
        print(nums)
arr = [[1,3],[2,6],[8,10],[15,18]]
# val = 9
k = Solution().merge(arr)
print(k)
        
# https://leetcode.com/problems/template/
