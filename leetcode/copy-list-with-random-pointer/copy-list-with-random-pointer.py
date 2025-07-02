from typing import List, Optional

# _ solution
# Time O() | Space O()


# Definition for a Node with 'next' and 'random' pointers.
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        result = []
        visited = set()
        current = self
        while current and current not in visited:
            visited.add(current)
            rand_val = current.random.val if current.random else None
            result.append(f"[{current.val},R:{rand_val}]")
            current = current.next
        return "->".join(result)


# Helper to create a linked list with `random` pointers from LeetCode-style input
def create_linked_list(arr):
    if not arr:
        return None

    nodes = [Node(val) for val, _ in arr]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    for i, (_, rand_index) in enumerate(arr):
        if rand_index is not None:
            nodes[i].random = nodes[rand_index]

    return nodes[0]  # return head


# Helper to print the linked list with random pointers
def print_linked_list(head):
    current = head
    result = []
    while current:
        rand_val = current.random.val if current.random else None
        result.append(f"[{current.val}, R:{rand_val}]")
        current = current.next
    print("->".join(result))


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        index_map = dict()
        current = head
        counter = 0
        nhead = Node(0)
        ncurrent = nhead
        nindex_map = dict()
        while current:
            index_map[counter] = current
            current = current.next
            counter += 1

        node_map = {v: k for k, v in index_map.items()}
        
        for i in range(counter):
            curr = index_map[i]
            nhead.next = Node(curr.val)
            nindex_map[i] = nhead.next

        for i in range(counter):
            curr = index_map[i]
            r_index = node_map[curr.random]
            nindex_map[i].random = nindex_map[r_index]




        ##
        # print(nums)


arr = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
head = create_linked_list(arr)

# val = 9
k = Solution().copyRandomList(head)
print(k)

# https://leetcode.com/problems/copy-list-with-random-pointer/
