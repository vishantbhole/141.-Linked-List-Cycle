# 141. Linked List Cycle
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def hasCycle(self, head):
        seen = []
        curr = head
        while curr:
            if curr in seen:
                return True
            seen.append(curr)
            curr = curr.next
        return False
