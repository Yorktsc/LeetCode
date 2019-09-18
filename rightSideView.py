# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, queue = [], [root]
        while queue:
            size = len(queue)
            res.append(queue[-1].val)
            for _ in range(size):
                curr = queue.pop(0)
                if curr.left:queue.append(curr.left)
                if curr.right:queue.append(curr.right)
        return res
            
