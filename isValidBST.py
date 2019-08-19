# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #Recursion
        """
        def helper(root, lower = -float("inf"), upper = float("inf")):
            if not root: return True
            if root.val <= lower or root.val >= upper: return False
            if (root.left and root.left.val >= root.val) or (root.right and root.right.val <= root.val):
                return False
            else:
                return helper(root.right, lower = root.val, upper = upper) and helper(root.left, lower = lower, upper = root.val)
        return helper(root)
        """
        
        #BFS
        """
        if not root: return True
        q = [(root, -float("inf"), float("inf"))]
        while q:
            root, lower, upper= q.pop()
            if not root: continue
            val = root.val
            if val <= lower or val >= upper: return False
            q.append((root.left, lower, val))
            q.append((root.right, val, upper))
        return True
        """
        
        #InOrder
        stack, inOrder = [], float("-inf")
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inOrder:
                return False
            inOrder = root.val
            root = root.right
        return True
        
