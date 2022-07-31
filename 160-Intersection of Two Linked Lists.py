# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, a: ListNode, b: ListNode) -> Optional[ListNode]:
        alen = self.getLength(a)
        blen = self.getLength(b)
        
        if alen < blen:
            alen, blen = blen, alen
            a, b = b, a
            
        diff = alen - blen
        for _ in range(diff):
            a = a.next
            
        while a and b:
            if a is b:
                return a
            
            a = a.next
            b = b.next        
        
        return None
        
    def getLength(self, head):
        count = 0
        
        while head:
            count += 1
            head = head.next
        
        return count
        
