from typing import List, Optional

# optmized solution
# Time O(m+n) | Space O(m+n)
# Iterative approach, we create a new linkedlist node and keep adding the smallest node into it.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        tail = head
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 is not None else list2
        return head.next

## 
        print(nums)
# arr = [2, 7, 11, 15]
# k = Solution().method_template(arr)
# print(k)
        
# https://leetcode.com/problems/merge-two-sorted-lists/
