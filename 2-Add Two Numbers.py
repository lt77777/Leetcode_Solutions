# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = str(self.getNum(l1) + self.getNum(l2))
        print(num)
        rtn = ListNode(val=int(num[-1]))
        curr = rtn
        for i in range(-2, -(len(num))-1, -1):
            curr.next = ListNode(val=int(num[i]))
            curr = curr.next
        return rtn
            
    
    def getNum(self, l):
        rtn = []
        curr = l
        rtn.append(curr.val)
        while curr.next:
            rtn.append(curr.next.val)
            curr = curr.next
        rtn.reverse()
        print(rtn)
        num = 0
        for i in range(len(rtn)):
            num += rtn[i] * 10**(len(rtn)-i-1)
        return num
