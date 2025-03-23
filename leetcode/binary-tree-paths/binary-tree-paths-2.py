from typing import List, Optional

# Optimized solution (Recursive)
# Time O(n) | Space O(n)
# 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        paths = []
        stack  = [(root, str(root.val))]

        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, f'{path}->{node.left.val}'))
            if node.right:
                stack.append((node.right, f'{path}->{node.right.val}'))
        return paths

## 
        print(nums)
arr = TreeNode(3)
k = Solution().binaryTreePaths(arr)
print(k)
        
# https://leetcode.com/problems/binary-tree-paths/
