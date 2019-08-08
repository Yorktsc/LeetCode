class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # head = [4,5,1,9], node = 5
        delete_node = node.next
        node.val = delete_node.val
        node.next = delete_node.next 
        
        #笨逼方法：修改所有nodes  
        """
        while node:
            if not node.next.next:
                node.val = node.next.val
                node.next = None
            else:
                node.val = node.next.val
            node = node.next
        """
