# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        if not root: return []
        res = []
        queue = [root]
        depth = 1
        while len(queue) > 0:
            tmp = []
            next_level = []
            for node in queue:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if depth % 2 == 0:
                tmp = tmp[::-1]
            res.append(tmp)
            queue = next_level
            depth += 1
        return res
        """
        res = []
        
        def helper(root, depth):
            if not root: return 
            if len(res) == depth:
                res.append([])
            if depth % 2 == 0:res[depth].append(root.val)
            else: res[depth].insert(0, root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        helper(root, 0)
        return res
