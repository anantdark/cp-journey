from typing import List, Optional

# optimized solution
# Time O(n) | Space O(1)
# We can use Floyd Cycle Detection algorithm with two pointers tortoise and hare moving at separate speeds, if they meet then we have a cycle.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr1 = head
        ptr2 = head
        while ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            if ptr1 == ptr2:
                return True
        return False

## 
        print(nums)
# arr = [2, 7, 11, 15]
# k = Solution().hasCycle()
# print(k)
        
# https://leetcode.com/problems/linked-list-cycle/
