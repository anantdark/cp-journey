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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = slow = fast = head

        if not head.next:
            return head.next

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        prev.next = slow.next
        return head

        ##
        print(nums)


arr = [1, 3, 4, 7, 1, 2, 6]
head = create_linked_list(arr)
k = Solution().deleteMiddle(head)
print(k)

# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
