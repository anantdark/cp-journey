from typing import List, Optional

# optmized solution (Recursive)
# Time O(n) | Space O(n)
# 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            
            if not (traverse(node1.left, node2.left)):
                return False
            
            if not (traverse(node1.right, node2.right)):
                return False
            
            return True
        return traverse(p, q)

## 
        print(nums)
arr = TreeNode(3)
arr1 = TreeNode(3)
k = Solution().isSameTree(arr, arr1)
print(k)
        
# https://leetcode.com/problems/same-tree/
