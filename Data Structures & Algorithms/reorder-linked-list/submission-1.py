# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast != None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next=None
        slow = temp
        def reverse(head1):
            if head1==None:
                return head1
            prev = None
            curr = head1
            while curr!=None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        reverse_head = reverse (slow)

        # def merge(head1, head2):
        #     while head1 and head2:
        #         next1 = head1.next
        #         next2 = head2.next

        #         head1.next = head2
        #         head2.next = next1

        #         head1 = next1
        #         head2 = next2
        def merge(head1, head2):
            dummy = ListNode()
            tail = dummy

            take_first = True

            while head1 and head2:
                if take_first:
                    tail.next = head1
                    head1 = head1.next
                else:
                    tail.next = head2
                    head2 = head2.next

                tail = tail.next
                take_first = not take_first

            if head1:
                tail.next = head1

            if head2:
                tail.next = head2

        merge(head , reverse_head)
