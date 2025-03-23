from typing import List, Optional

# Optimized solution (Iterative)
# Time O(n) | Space O(n)
# In a standard preorder traversal, we visit the root node before we visit the left and right subtrees. However, postorder traversal requires us to visit the left and right subtrees before the root node. We can adapt the preorder traversal by visiting nodes in the order of root, right subtree, and then left subtree. Reversing the resulting list from this modified preorder traversal gives us the correct postorder sequence. We use a stack to traverse the tree iteratively, starting with the root node. We push the current node onto the stack and add its value to the result list. Instead of moving to the left child, we move to the right child. If there's no right child, we pop a node from the stack and move to its left child. This approach processes the right subtree before the left subtree, aligning with the modified preorder traversal. After traversing the entire tree, we reverse the result list to get the postorder sequence: left subtree, right subtree, root.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node, arr=[]):
            stk = [node]

            while stk:
                node = stk.pop()
                arr.append(node.val)
                if node.left: stk.append(node.left)
                if node.right: stk.append(node.right)
            return arr[::-1]
        if root:
            return traverse(root)
        else:
            return []

## 
        print(nums)
arr = TreeNode(3)
k = Solution().postorderTraversal(arr)
print(k)
        
# https://leetcode.com/problems/binary-tree-postorder-traversal/
