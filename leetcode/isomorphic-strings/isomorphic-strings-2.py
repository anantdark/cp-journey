from typing import List, Optional

# Optimized solution
# Time O() | Space O()
# When strings are put in set, we get unique characters, and when zipped we get pairs for characters and their set would also give unique pairs. So if the number of unique characters in both string is equal to the number of unique pairs then it would be isomorphic string.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

## 
        print(nums)
s = 'paper'
t = 'title'
k = Solution().isIsomorphic(s, t)
print(k)
        
# https://leetcode.com/problems/isomorphic-strings/
