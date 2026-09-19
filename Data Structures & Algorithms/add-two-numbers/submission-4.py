# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode=ListNode(-1)
        curr=dummyNode
        carry=0
        while (l1 or l2):
            if l1 != None:
                val1 = l1.val
            else:
                val1 = 0
            if l2 != None:
                val2 = l2.val
            else:
                val2 = 0
            summ=carry+(val1+val2)
            newNode=ListNode(summ%10)
            curr.next=newNode
            curr=curr.next
            carry=(summ) // 10
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if carry:
            newNode=ListNode(carry)
            curr.next=newNode
            curr=curr.next
        return dummyNode.next


