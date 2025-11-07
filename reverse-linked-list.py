# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        previous_node: ListNode | None = None
        while node:
            node.next, previous_node, node = previous_node, node, node.next
        return previous_node
