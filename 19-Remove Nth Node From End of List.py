# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.getLen(head)
        if length == 1:
            return None
        index = length - n
        if index == 0:
            return head.next
        i = 0
        curr = head
        while i < index:
            if i == index-1:
                if n == 0:
                    curr.next = None
                    break
                curr.next = curr.next.next
            curr = curr.next
            i += 1
        return head
        
    def getLen(self, head):
        i = 1
        while head.next:
            i += 1
            head = head.next
        return i
