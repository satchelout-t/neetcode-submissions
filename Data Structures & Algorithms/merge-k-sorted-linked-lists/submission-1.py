class Solution:
    def merge2(self, head1, head2):
        dummy = ListNode(-1)
        curr = dummy

        while head1 and head2:
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next

            curr = curr.next

        curr.next = head1 if head1 else head2

        return dummy.next

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                head1 = lists[i]
                head2 = lists[i + 1] if i + 1 < len(lists) else None

                merged.append(self.merge2(head1, head2))

            lists = merged

        return lists[0]