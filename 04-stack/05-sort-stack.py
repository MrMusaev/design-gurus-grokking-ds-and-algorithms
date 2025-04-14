class Solution:
    def sortStack(self,stack):
        tempStack = []
        while stack:
            tmp = stack.pop()
            while tempStack and tempStack[-1] > tmp:
                stack.append(tempStack.pop())
            tempStack.append(tmp)
        
        return tempStack

# Tests with assertions
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([34, 3, 31, 98, 92], [3, 31, 34, 92, 98]),
        ([1, 2, 3], [1, 2, 3]),
        ([5, 4, 3], [3, 4, 5]),
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([1, -1, 0], [-1, 0, 1]),
        ([10], [10]),
        ([], []),
    ]

    for (input_stack, expected) in test_cases:
        result = sol.sortStack(input_stack)
        print(f"Input: {input_stack}, Expected: {expected}, Result: {result}, Passed: {expected == result}")