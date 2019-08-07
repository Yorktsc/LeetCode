class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid, slow.next = slow.next, None
        left, right = self.sortList(head), self.sortList(mid)
        res = h = ListNode(233)
        while left and right:
            if left.val < right.val:
                h.next, left = ListNode(left.val), left.next
                h = h.next
            else:
                h.next, right = ListNode(right.val), right.next
                h = h.next
        h.next = left if right is None else right
            
        return res.next
