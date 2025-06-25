class Solution:
    def reverseQueue(self, q):
        prev_node = None
        current_node = q
        while current_node:
            # We have prev, current, next nodes now 
            # If current_node is the last element then the next_node is None 
            next_node = current_node.next
            # From prev -> current to prev <- current 
            current_node.next = prev_node
            # Shifting prev to the left
            prev_node = current_node
            # Shifting current to the left
            current_node = next_node
        
        return q

# Tests with assertions
if __name__ == "__main__":
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    # Helper function to create a linked list from a list
    def create_linked_list(values):
        if not values:
            return None
        head = Node(values[0])
        current = head
        for value in values[1:]:
            current.next = Node(value)
            current = current.next
        return head

    # Helper function to convert linked list to a list
    def linked_list_to_list(head):
        result = []
        while head:
            result.append(head.value)
            head = head.next
        return result

    sol = Solution()
    test_cases = [
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([10, 20, 30], [30, 20, 10]),
        ([5], [5]),
        ([], []),
        ([1, 2, 3], [3, 2, 1]),
        ([100, 200], [200, 100]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([0], [0]),
        ([1], [1]),
        ([2, 4], [4, 2]),
        ([3, 6, 9], [9, 6, 3]),
        ([7, 8], [8, 7]),
        ([5], [5]),
        ([], []),
    ]

    for input_list, expected in test_cases:
        linked_list = create_linked_list(input_list)
        reversed_list = sol.reverseQueue(linked_list)
        result = linked_list_to_list(reversed_list)
        assert result == expected, f"Expected {expected}, but got {result}"
    
    print("All tests passed!")