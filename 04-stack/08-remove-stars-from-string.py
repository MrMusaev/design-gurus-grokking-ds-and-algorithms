class Solution:
    def removeStars(self, s):
        stack = []
        for c in s:
            if stack and c == '*':
                stack.pop()
            elif c != "*":
                stack.append(c)

        result = ""
        while stack:
            result = stack.pop() + result

        return result

# Tests with assertions
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("leet**cod*e", "lecoe"),
        ("erase*****", ""),
        ("abc*de*fgh", "abdfgh"),
        ("a*b*c*d", "d"),
        ("", ""),
        ("a", "a"),
        ("*", ""),
    ]

    for input_str, expected in test_cases:
        result = sol.removeStars(input_str)
        assert result == expected, f"Expected {expected}, but got {result}"
    print("All tests passed!")