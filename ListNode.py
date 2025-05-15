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
def create_linked_list(values, pos):
    if not values:
        return None

    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]
