from typing import List, Optional

# better solution
# Time O(n) | Space O(n)
# We are maintaing a dict with nodes and checking if we are encountering the node again to detect cycle.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        while head:
            if visited.get(head):
                return True
            else:
                visited[head] = True
            head = head.next
        return False

## 
        print(nums)
arr = [2, 7, 11, 15]
# k = Solution().hasCycle()
# print(k)
        
# https://leetcode.com/problems/linked-list-cycle/
