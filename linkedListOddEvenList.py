# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 1->2->3
        # 1->2->3->4
        # 1->2->3->4->5
        """
        if not head:return head
        node = head
        one = ListNode(None)
        two = ListNode(None)
        one_link = one
        two_link = two
        i = 1
        while node:
            #pre = node.next
            if i%2==1:
                one.next = node
                one = one.next
                #node = node.next
            else:
                two.next = node
                two = two.next
            node = node.next
            i+=1
        two.next = None
        one.next = two_link.next
        return one_link.next
        """
        if not head or not head.next or not head.next.next:
            return head
        odd_head = odd = ListNode(None)
        even_head = even = ListNode(None)
        i = 1
        while head:
            if i & 1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            i += 1
            head = head.next
        even.next = None
        odd.next = even_head.next
        return odd_head.next
