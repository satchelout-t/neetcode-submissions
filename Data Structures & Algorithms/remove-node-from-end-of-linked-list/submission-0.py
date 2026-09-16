# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head
        fast=head
        temp=head
        for i in range(n):
            fast=fast.next
        if fast==None:
            newHead=head.next
            head.next=None
            return newHead
        while(fast.next):
            slow=slow.next
            fast=fast.next
        deleteNode=slow.next
        slow.next=deleteNode.next
        deleteNode.next=None
        return head

        