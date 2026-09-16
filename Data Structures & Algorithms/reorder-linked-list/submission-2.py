# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return
        #1st part finding Middle
        middle=head
        fast=head
        while fast.next and fast.next.next:
            middle=middle.next
            fast=fast.next.next
        
        #2nd part reverse 
        second_head=middle.next
        middle.next=None
        nxt=second_head.next
        second_head.next=None
        prev=second_head
        curr=prev
        while nxt:
            curr=nxt
            nxt=nxt.next
            curr.next=prev
            prev=curr
        second_head=curr
        #3rd part
        temp1=prev1=head
        temp2=prev2=second_head
        while prev2:
            temp1=temp1.next
            prev1.next=prev2
            prev1=temp1
            temp2=temp2.next
            prev2.next=prev1
            prev2=temp2
       

            

            
