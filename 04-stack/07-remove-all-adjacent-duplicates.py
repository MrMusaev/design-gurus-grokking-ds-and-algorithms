class Solution:
    def removeDuplicates(self, s):
        stack = []

        for i, c in enumerate(s):
            if not stack:
                stack.append(c)
                continue
            if c == stack[-1]:
                stack.pop()
                continue
            stack.append(c)
        
        result = ""
        while stack:
            result = stack.pop() + result

        return result

# Tests with assertions
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("abbaca", "ca"),
        ("azxxzy", "ay"),
        ("", ""),
        ("a", "a"),
        ("aa", ""),
        ("abccba", ""),
        ("abcdeedcba", ""),
    ]

    for input_str, expected in test_cases:
        result = sol.removeDuplicates(input_str)
        assert result == expected, f"Expected {expected}, but got {result}"
    print("All tests passed!")