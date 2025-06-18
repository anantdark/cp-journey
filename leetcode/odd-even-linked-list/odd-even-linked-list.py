from typing import List, Optional

# _ solution
# Time O() | Space O()

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
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        even_head = head.next
        odd = head
        even = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head

## 
        print(nums)
arr = [1,2,3,4,5,6,7, 8]
head = create_linked_list(arr)
print_linked_list(head)
# val = 9
k = Solution().oddEvenList(head)
print(k)
        
# https://leetcode.com/problems/odd-even-linked-list/
