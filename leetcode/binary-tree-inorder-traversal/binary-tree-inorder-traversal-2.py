from typing import List, Optional

# Optimized solution (Recursive)
# Time O(n) | Space O(n) (recursive stack)
# 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node, arr=[]):
            if not node:
                return
            
            traverse(node.left)
            arr.append(node.val)
            traverse(node.right)
            return arr
        if root:
            return traverse(root)
        else:
            return []

## 
        print(nums)
arr = TreeNode(3)
k = Solution().inorderTraversal(arr)
print(k)
        
# https://leetcode.com/problems/binary-tree-inorder-traversal/
