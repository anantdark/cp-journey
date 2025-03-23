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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stk = []
        curr = root
        while curr or stk:
            while curr:
                stk.append(curr)
                curr = curr.left
            curr = stk.pop()
            ans.append(curr.val)
            curr = curr.right
        return ans

## 
        print(nums)
arr = TreeNode(3)
k = Solution().inorderTraversal(arr)
print(k)
        
# https://leetcode.com/problems/binary-tree-inorder-traversal/
