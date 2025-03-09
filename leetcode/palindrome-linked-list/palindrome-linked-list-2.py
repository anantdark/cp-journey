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
    def reverse(self, head):
        if not (head and head.next):
            return head
        
        new_head = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return new_head
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find middle
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #reverse after middle
        new_head = self.reverse(slow.next)
        ptr1 = head
        ptr2 = new_head

        # traverse both sub-lists
        while ptr2:
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return True
## 
        print(nums)
arr = [2, 7, 11, 15]
k = Solution().isPalindrome(arr)
print(k)
        
# https://leetcode.com/problems/palindrome-linked-list/
