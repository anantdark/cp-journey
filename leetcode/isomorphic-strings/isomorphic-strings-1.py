from typing import List, Optional

# Optimized solution
# Time O(n) | Space O(n)
# We can map each character in s to a character in t, for each index we can check if both are mapped to the same character in t. In else we also need to handle the case where character in t is already mapped, but s has no mapping at the index.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        for i, ch in enumerate(s):
            if ch in hashmap.keys():
                if hashmap[ch] != t[i]:
                    return False
            else:
                if t[i] in hashmap.values():
                    return False
                else:
                    hashmap[ch] = t[i]
        return True

## 
        print(nums)
s = 'paper'
t = 'title'
k = Solution().isIsomorphic(s, t)
print(k)
        
# https://leetcode.com/problems/isomorphic-strings/
