from typing import List, Optional

# Optmized solution
# Time O(n) | Space O(1)
# In this problem, we can use two pointers and move from opposite ends, if the characters are not equal, we can check if the substring from i+1 to j is a palindrome or from i to j-1 is a palindrome, since we can remove at most 1 character. If it is a palindrome, we can return True. Otherwise, we can return False.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        
        palindrome = lambda x: x == x[::-1]

        i, j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if palindrome(s[i+1: j+1]) or palindrome(s[i:j]):
                    return True
                else:
                    return False
        return True

## 
        print(nums)
arr = 'abbac'
k = Solution().validPalindrome(arr)
print(k)
        
# https://leetcode.com/problems/valid-palindrome-ii/
