# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_node, fast_node = head, head.next
        while True:
            if fast_node:
                if fast_node.next:
                    slow_node, fast_node = slow_node.next, fast_node.next.next
                else:
                    return slow_node.next
            else:
                return slow_node
