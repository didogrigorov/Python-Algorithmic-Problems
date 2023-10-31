class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous, current = dummy, head

        while current and current.next:
            next_pair = current.next.next
            second = current.next

            second.next = current
            current.next = next_pair

            previous.next = second

            previous = current
            current = next_pair

        return dummy.next