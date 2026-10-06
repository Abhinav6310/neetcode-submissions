# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        temp = dummy
        while temp.next != None:
            if temp.next.val == val:
                a = temp.next.next
                temp.next = None
                temp.next = a
            else:
                temp = temp.next
        
        return dummy.next

