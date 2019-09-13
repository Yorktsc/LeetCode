"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def __init__(self):
        self.visited = {}
        
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        #Approach1 Map
        m = {}
        curr = res = Node(None, None, None)
        while head:
            if head in m.keys():
                tmp = m[head]
            else:
                tmp = Node(head.val, None, None)
                m[head] = tmp
            curr.next = tmp 
            curr = curr.next
            if head.random:
                if head.random in m.keys():
                    random = m[head.random]
                else:
                    random = Node(head.random.val, None, None)
                    m[head.random] = random
                curr.random = random
            head = head.next
        
        return res.next
        """
        
        #Approach2 Recursive
        if not head: return head
        if head in self.visited.keys():
            return self.visited[head]
        
        node = Node(head.val, None, None)
        
        self.visited[head] = node
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node
