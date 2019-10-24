# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        """
        def has_child(root, target): // too inefficient
            if not root: 
                return False
            if root.val == target:
                return True
            else:
                return has_child(root.left, target) or has_child(root.right, target)
        
        if root == p or root == q:
            return root
        
        if has_child(root.left, q.val) and has_child(root.left, p.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif has_child(root.right, q.val) and has_child(root.right, p.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        """
        """
        def recurseTree(root):
            if not root:
                return False 
            
            left = recurseTree(root.left)
            right = recurseTree(root.right)
            
            mid = root == p or root == q
            
            if mid + left + right >= 2:
                self.ans = root
            
            return mid or left or right
        
        recurseTree(root)
        return self.ans
        """
        
        
        child2parent = {}
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left: 
                child2parent[node.left.val] = node.val
                queue.append(node.left)
            if node.right:
                child2parent[node.right.val] = node.val
                queue.append(node.right)
        seen = set()
        seen.add(p.val)
        p_val = p.val
        while p_val in child2parent.keys():
            p_val = child2parent[p_val]
            seen.add(p_val)
        q_val = q.val
        while q_val in child2parent.keys():
            if q_val in seen:
                return TreeNode(q_val)
            q_val = child2parent[q_val]
        if q_val == root.val:
            return root
        return None
