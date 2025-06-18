from typing import List
import heapq

# Optimal solution
# Time O(KlogK) | Space O(K)
# Since both lists are sorted the first smallest pair will be from index (0,0), after than we can either increment i or j which will give rise to 2 cases. Assume one of the cases to be the next smallest pair, then we will again have 2 new choices either to increment i or j, but the remaining pair from before also needs to be considered. At each step we need to compare new steps as well as old pairs left for finding pair with minimum sum. For this we use a heap, we push both the possible pairs in a min-heap and then pull the minimum pair each time and continue from there.

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        i, j = 0, 0
        pairset = {(i, j)}
        final = []
        heap = []
        heapq.heappush(heap, (nums1[i]+nums2[j], (i, j)))
        while heap and len(final) < k:
            top = heapq.heappop(heap)
            i, j = top[1]
            final.append([nums1[i], nums2[j]])
            if (i+1) < len(nums1) and (i+1, j) not in pairset:
                heapq.heappush(heap, (nums1[i+1]+nums2[j], (i+1, j)))
                pairset.add((i+1, j))
            
            if (j+1) < len(nums2) and (i, j+1) not in pairset:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], (i, j+1)))
                pairset.add((i, j+1))
        return final

## 
        print(nums)
arr1 = [1,7,11]
arr2 = [2,4,6]
val = 2
k = Solution().kSmallestPairs(arr1,arr2, val)
print(k)
        
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
