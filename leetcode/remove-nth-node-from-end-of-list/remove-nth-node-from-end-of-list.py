from typing import List, Optional

# Optimal solution
# Time O(N) | Space O(1)


# Helper to create a linked list from a Python list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper to print the linked list (optional)
def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        nodes = []
        current = self
        while current:
            nodes.append(str(current.val))
            current = current.next
            if len(nodes) > 100:  # avoid infinite loops
                nodes.append("...")
                break
        return "->".join(nodes)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        ptr1 = ptr2 = head
        while n and ptr2:
            ptr2 = ptr2.next
            n -= 1
        while ptr2 and ptr2.next:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        
        if not ptr2:
            head = head.next
        else:
            ptr1.next = ptr1.next.next
        return head

        ##
        print(nums)


arr = [1]
head = create_linked_list(arr)
val = 1
k = Solution().removeNthFromEnd(head, val)
print(k)

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
