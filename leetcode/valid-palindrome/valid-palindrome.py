from typing import List, Optional, bool

# _ solution
# Time O() | Space O()
# 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr1, ptr2 = 0, len(s)-1

        if len(s) < 2:
            return True
        
        def check_palindrome(s, ptr1, ptr2):
            while ptr1 < len(s) and not s[ptr1].isalnum():
                ptr1 += 1
            while ptr2 > 0 and not s[ptr2].isalnum():
                ptr2 -= 1
            if not(ptr1 < len(s) and ptr2) > 0:
                return True
            if not s[ptr1].lower() == s[ptr2].lower():
                return False
            else:
                ptr1 += 1
                ptr2 -= 1
                if ptr1 >= ptr2:
                    return True
                else:
                    return check_palindrome(s, ptr1, ptr2)

        return check_palindrome(s, ptr1, ptr2)
        

## 
        # print(nums)
arr = "A man, a plan, a canal: Panama"
k = Solution().isPalindrome(arr)
print(k)
        
# https://leetcode.com/problems/valid-palindrome/
