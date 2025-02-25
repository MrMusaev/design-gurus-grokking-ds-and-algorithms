class Solution:
    def reverseString(self, s):
        stack = list(s)
        
        reverse_s = ''

        while stack:
            reverse_s += stack.pop()

        return reverse_s


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = {
        "hello" : "olleh",
        "world" : "dlrow",
        "python" : "nohtyp",
        "" : ""
    }
    
    for s, expected in test_cases.items():
        result = solution.reverseString(s)
        print(f"Input: {s}, Expected: {expected}, Result: {result}, Passed: {expected == result}")
    