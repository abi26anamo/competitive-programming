class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([(root.left,root.right)])
        while queue:
            node1,node2 = queue.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val!=node2.val:
                return False
            queue.append((node1.right,node2.left))
            queue.append((node1.left,node2.right))
        return True
    
