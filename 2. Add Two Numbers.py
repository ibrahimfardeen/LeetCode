# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        next1 = l1
        next2 = l2   
        x = ''
        y = ''
        while next1 != None or next2 != None:
            x += str(next1.val) if next1 else '0'
            y += str(next2.val) if next2 else '0'
            next1 = next1.next if next1 else None 
            next2 = next2.next if next2 else None
          
        a = str(int(str(x)[::-1]) + int(str(y)[::-1]))
        l = ListNode()
        temp = l
        
        for i in a[::-1]:
            temp.next = ListNode(i)
            temp = temp.next
        return l.next
