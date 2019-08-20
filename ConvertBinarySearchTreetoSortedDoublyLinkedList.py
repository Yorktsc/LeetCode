"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        #Iteratively InOrder
        """
        if not root: return None
        stack, curr, res = [], root, []
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            res.append(node.val)
            curr = node.right
        curr = head = Node(None, None, None)
        prev = None
        for i in range(len(res)):
            curr.val = res[i]
            curr.left = prev
            prev = curr
                
            if i < len(res) - 1:
                curr.right = Node(None,None,None)
                curr = curr.right
            else:
                curr.right = head
        head.left = curr
        return head
        """
        
        last, first = None
        #Recursion + python3
        def helper(node):
            nonlocal last, first
            if node:
                helper(node.left)
                if last:
                    last.right = node
                    node.left = last
                else: 
                    first = node
                last = node
                helper(node.right)
        helper(root)
        if not root: return None
        last.right, first.left  = first, last
        return first
