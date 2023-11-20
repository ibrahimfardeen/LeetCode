# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        b = []
        temp1 = list1
        temp2 = list2
        while temp1 != None:
            a.append(temp1.val)
            temp1 = temp1.next
        while temp2 != None:
            b.append(temp2.val)
            temp2 = temp2.next
        c = sorted(a + b)
        dummy = ListNode()
        temp = dummy
        for i in c:
            temp.next = ListNode(i)
            temp = temp.next
        return dummy.next
