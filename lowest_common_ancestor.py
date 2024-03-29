# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if not node:
                return None
            
            if p == node or q == node:
                return node  

            left = dfs(node.left) 
            right = dfs(node.right) 

            if left and right:
                return node 
            else:
                return left if left else right
        return dfs(root)     
