# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        dummy = ListNode()
        temp = ListNode()
        dummy.next = temp
        carry = 0
        while cur1!=None or cur2!=None:
            if cur1!=None:
                val1 = cur1.val
                cur1 = cur1.next
            else:
                val1 = 0

            if cur2!=None:
                val2 = cur2.val
                cur2 = cur2.next
            else:
                val2 = 0
            
            val = val1+val2+carry
            if val>=10:
                carry = val//10
                val = val%10
            else:
                carry=0
            temp.val = val
            if cur1 ==None and cur2 ==None and carry==0:
                temp.next = None
            else:
                temp.next = ListNode()
                temp = temp.next

            
        if carry!=0:
            temp.val = carry
        
        
        return dummy.next
            
                