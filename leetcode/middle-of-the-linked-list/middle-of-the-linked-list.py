from typing import List, Optional

# Optimized solution
# Time O(n) | Space O(1)
# 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow if fast.next is None else slow.next

## 
        print(nums)
arr = [2, 7, 11, 15]
k = Solution().middleNode(arr)
print(k)
        
# https://leetcode.com/problems/middle-of-the-linked-list/
