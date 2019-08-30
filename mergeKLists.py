from Queue import PriorityQueue
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        #PriorityQueue
        """
        res = curr = ListNode("fuck")
        q = PriorityQueue()
        
        for l in lists:
            if l:
                q.put((l.val, l))
        
        while not q.empty():
            val, node = q.get()
            curr.next = ListNode(val)
            curr = curr.next
            node = node.next
            if node:
                q.put((node.val, node))
        return res.next
        """
        
        #Divide and Conquer
        k = len(lists)
        interval = 1
        while interval < k:
            for i in range(0, k - interval, interval*2):
                lists[i] = self.merge2Lists(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] if k > 0 else lists
        
        
        
        
    
    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next
