from typing import List, Optional

# Optimal solution
# Time O() | Space O()
# 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_head = ListNode()
        curr = l1_head
        carry = 0
        while l1 or l2:
            sum = carry
            sum += l1.val if l1 else 0
            sum += l2.val if l2 else 0
            carry = sum // 10
            sum %= 10
            node = ListNode(sum)
            curr.next = node
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            curr.next = ListNode(carry)
        return l1_head.next

## 
        print(nums)
arr = [2, 7, 11, 15]
k = Solution().addTwoNumbers(arr, arr)
print(k)
        
# https://leetcode.com/problems/add-two-numbers/
