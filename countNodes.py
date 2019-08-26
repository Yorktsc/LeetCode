# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Brute Force
        """
        if not root: return 0
        count = []
        def helper(root):
            if root:
                count.append(root.val)
                helper(root.left)
                helper(root.right)
        helper(root)
        return len(count)
        """
        
        #Complete Tree Nodes
        if not root: return 0
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        if left == right:
            return 2 ** left + self.countNodes(root.right)
        else:
            return 2 ** right + self.countNodes(root.left)
    
    def getDepth(self, root):
        d = 0
        while root:
            root = root.left
            d += 1
        return d
    
