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
    def template(self, nums: List[int], target: int):

        ##
        print(nums)


arr = [2, 7, 11, 15]
val = 9
k = Solution().template(arr, val)
print(k)

# https://leetcode.com/problems/template/
