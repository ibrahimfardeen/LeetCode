# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        x = []
        temp = head
        while temp != None:
            if temp.val not in x:
                x.append(temp.val)
            temp = temp.next
        l = ListNode
        dummy = l
        for i in x:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return l.next
