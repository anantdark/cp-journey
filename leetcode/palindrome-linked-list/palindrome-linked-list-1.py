from typing import List, Optional

# Brute solution (Iterative)
# Time O(n) | Space O(n)
# 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        curr = head
        for i in arr[::-1]:
            if curr.val != i:
                return False
            else:
                curr = curr.next
                continue
        if curr:
            return False
        return True

## 
        print(nums)
arr = [2, 7, 11, 15]
k = Solution().isPalindrome(arr)
print(k)
        
# https://leetcode.com/problems/palindrome-linked-list/
