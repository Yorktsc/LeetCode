class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 1->2->3->4->5
        # 3->4->5
        if not head or not head.next:
            return True
        slow = fast = head
        while slow and fast:
            slow = slow.next 
            fast = fast.next.next if fast.next is not None else fast.next
        # Reverse slow as head
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
