class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_copy = {None: None}

        # first pass
        curr = head
        while curr:
            copy = Node(curr.val)
            old_copy[curr] = copy
            curr = curr.next

        # second pass - create random connections
        curr = head
        while curr:
            copy = old_copy[curr]
            copy.next = old_copy[curr.next]
            copy.random = old_copy[curr.random]
            curr = curr.next

        return old_copy[head]