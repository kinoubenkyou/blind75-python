# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node1: ListNode = head
        node2: ListNode = head
        while node2 and node2.next:
            node1 = node1.next
            node2 = node2.next.next
            if node1 == node2:
                return True
        return False
