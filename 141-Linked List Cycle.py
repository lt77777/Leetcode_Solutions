# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = 0
        if not head:
            return False
        while head.next:
            head = head.next
            i += 1
            if i > 10000:
                return True
        return False
