from typing import List, Optional

# Optimal solution
# Time O(max(n, m)) | Space O(max(n, m))
# We can traverse any one linked list and put its nodes in a hashmap, then when traversing the second linked list we can verify if the node is already traversed i.e. is common.


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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeset = set()
        currentA = headA
        currentB = headB
        inter = None
        while currentA:
            nodeset.add(currentA)
            currentA  = currentA.next
        
        while currentB:
            if currentB in nodeset:
                inter = currentB
                break
            currentB = currentB.next
        return inter

        ##
        print(nums)


arr = [2, 7, 11, 15]
val = 9
k = Solution().template(arr, val)
print(k)

# https://leetcode.com/problems/intersection-of-two-linked-lists/
