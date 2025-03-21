from typing import List

# Optimal solution
# Time O(S) S is the nums of all sting chars | Space O(1)
# 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(len(prefix)):
            for word in strs:
                if i == len(word) or prefix[i] != word[i]:
                    return prefix[:i]
        return prefix

## 
        # print(nums)
arr = ["flower", "flow", "flight"]
k = Solution().longestCommonPrefix(arr)
print(k)
        
# https://leetcode.com/problems/longest-common-prefix/
