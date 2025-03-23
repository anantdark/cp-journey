from typing import List, Optional

# Optimized solution
# Time O() | Space O()
# index() returns the first occurence of a character in string, when we map the method (s.index) for each char in s, we get the index of first occurence for the char. If the indexes are same for both strings, then it is isomorphic string.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]

## 
        print(nums)
s = 'paper'
t = 'title'
k = Solution().isIsomorphic(s, t)
print(k)
        
# https://leetcode.com/problems/isomorphic-strings/
