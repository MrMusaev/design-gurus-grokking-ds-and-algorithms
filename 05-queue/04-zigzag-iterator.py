from collections import deque

class Solution:
    def __init__(self, v1, v2):
        self.queue = deque()
        for v in (v1, v2):
            if v:
                self.queue.append((v, 0))  # Store (list, index) pairs
       
    def next(self):
        nextList, index = self.queue.popleft()
        
        if index >= len(nextList):
            return None
        
        value = nextList[index]
        index += 1

        if index < len(nextList):
            self.queue.append((nextList, index))
        
        return value
    
    def hasNext(self):
        return not len(self.queue) == 0
    
# Tests with assertions
if __name__ == "__main__":
    sol = Solution([1, 2, 3], [4, 5])
    expected_output = [1, 4, 2, 5, 3]
    result = []
    
    while sol.hasNext():
        result.append(sol.next())
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    
    # Additional test cases
    sol = Solution([1, 2], [3, 4, 5])
    expected_output = [1, 3, 2, 4, 5]
    result = []
    while sol.hasNext():
        result.append(sol.next())
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    sol = Solution([], [1, 2, 3])
    expected_output = [1, 2, 3]
    result = []
    while sol.hasNext():
        result.append(sol.next())
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    print("All tests passed!")