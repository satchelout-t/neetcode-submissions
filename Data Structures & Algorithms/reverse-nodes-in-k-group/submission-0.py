class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        prev_group = dummy

        while True:

            # 1. Find kth node
            kth = prev_group

            for _ in range(k):
                kth = kth.next

                if kth is None:
                    return dummy.next

            # Node after the current group
            next_group = kth.next

            # 2. Reverse current group
            prev = next_group
            curr = prev_group.next

            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # 3. Connect previous group to reversed group
            old_start = prev_group.next
            prev_group.next = kth

            # 4. old_start is now the end of reversed group
            prev_group = old_start