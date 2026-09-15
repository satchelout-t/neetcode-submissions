class Solution:
    def reorderList(self, head):
        if head == None or head.next == None:
            return

        # STEP 1: find the middle
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        # STEP 2: cut, then reverse the second half
        second = slow.next
        slow.next = None
        prev = None
        while second != None:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        second = prev

        # STEP 3: weave the halves
        first = head
        while second != None:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2