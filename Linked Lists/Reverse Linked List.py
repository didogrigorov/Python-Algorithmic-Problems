# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

def create_list() -> ListNode:
    tail = ListNode(5, None)
    node4 = ListNode(4, tail)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head = ListNode(1, node2)
    return head

if __name__ == '__main__':
    sol = Solution()
    head = create_list()
    result = sol.reverseList(create_list())
    print(result.next.next.val)