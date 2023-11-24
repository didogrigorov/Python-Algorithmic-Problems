class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        length, tail = 1, head

        while tail.next:
            tail = tail.next
            length += 1

        k = k % length

        if k == 0:
            return head

        current = head
        for i in range(length - k - 1):
            current = current.next

        new_head = current.next
        current.next = None
        tail.next = head
        return new_head