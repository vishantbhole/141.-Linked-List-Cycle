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

# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1: no cycle
    head1 = create_linked_list([3, 2, 0, -4], -1)
    print("Test case 1 (no cycle):", sol.hasCycle(head1))  # False

    # Test case 2: cycle at position 1 (node with value 2)
    head2 = create_linked_list([3, 2, 0, -4], 1)
    print("Test case 2 (cycle at pos 1):", sol.hasCycle(head2))  # True

    # Test case 3: single node, no cycle
    head3 = create_linked_list([1], -1)
    print("Test case 3 (single node, no cycle):", sol.hasCycle(head3))  # False

    # Test case 4: single node with cycle
    head4 = create_linked_list([1], 0)
    print("Test case 4 (single node with cycle):", sol.hasCycle(head4))  # True

    # Test case 5: empty list
    head5 = create_linked_list([], -1)
    print("Test case 5 (empty list):", sol.hasCycle(head5))  # False
