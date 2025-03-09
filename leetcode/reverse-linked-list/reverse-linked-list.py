from typing import List, Optional

# Optimized solution
# Time O(n) | Space O(n) recursion stack space
# 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

## 
        print(nums)
arr = [2, 7, 11, 15]
k = Solution().method_template(arr)
print(k)
        
# https://leetcode.com/problems/reverse-linked-list/
