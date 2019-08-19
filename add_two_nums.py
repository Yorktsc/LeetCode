class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head, carry = ListNode(None), 0
        result = head
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + carry
            num = s % 10
            head.next = ListNode(num)
            carry = s // 10
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            head = head.next
        if carry == 1:
            head.next = ListNode(1)
        return result.next
