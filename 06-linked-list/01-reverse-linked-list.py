class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if not head:
            return None
        
        current = head
        prev = None
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev
    

# Tests with assertions
if __name__ == "__main__":
    sol = Solution()
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Reverse the linked list
    reversed_head = sol.reverseList(head)
    
    # Check if the reversed linked list is correct
    assert reversed_head.val == 5
    assert reversed_head.next.val == 4
    assert reversed_head.next.next.val == 3
    assert reversed_head.next.next.next.val == 2
    assert reversed_head.next.next.next.next.val == 1
    assert reversed_head.next.next.next.next.next is None
    
    print("All tests passed!")