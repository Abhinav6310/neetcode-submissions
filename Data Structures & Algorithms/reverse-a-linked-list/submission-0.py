# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next==None:
            return head
        prev = None
        curr = head
        temp = curr.next
        while curr!=None:
            curr.next = prev
            prev = curr
            curr = temp
            if temp!=None:
                temp = temp.next
        return prev