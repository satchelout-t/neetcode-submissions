class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 1. Insert copied nodes after every original node
        curr = head

        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # 2. Set random pointers of copied nodes
        curr = head

        while curr:
            copy = curr.next

            if curr.random:
                copy.random = curr.random.next

            curr = copy.next

        # 3. Separate the original and copied lists
        curr = head
        copy_head = head.next

        while curr:
            copy = curr.next
            curr.next = copy.next

            if copy.next:
                copy.next = copy.next.next

            curr = curr.next

        return copy_head