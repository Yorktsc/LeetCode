class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #recursion way
        """
        def helper(root, res):
            if root:
                if root.left:
                    helper(root.left, res)
                res.append(root.val)
                if root.right:
                    helper(root.right, res)
        res = []
        helper(root, res)
        return res
        """
        #Iterative way
        res = []
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
