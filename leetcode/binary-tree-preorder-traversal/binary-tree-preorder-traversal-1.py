from typing import List, Optional

# Optimized solution (Iterative)
# Time O(n) | Space O(n)
# 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node, arr=[]):
            stk = [node]

            while stk:
                node = stk.pop()
                arr.append(node.val)
                if node.right: stk.append(node.right)
                if node.left: stk.append(node.left)
            return arr
        if root:
            return traverse(root)
        else:
            return []

## 
        print(nums)
arr = TreeNode(3)
k = Solution().preorderTraversal(arr)
print(k)
        
# https://leetcode.com/problems/binary-tree-preorder-traversal/
