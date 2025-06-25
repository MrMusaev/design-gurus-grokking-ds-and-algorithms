class Solution:
    def makeGood(self, s):
        result = []
        for c in s:
            if result and c.swapcase() == result[-1]:
                result.pop()
            else:
                result.append(c)

        return "".join(result)
    
# Tests with assertions
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("leEeetcode", "leetcode"),
        ("abBAcC", ""),
        ("s", "s"),
        ("", ""),
        ("aA", ""),
        ("aB", "aB"),
        ("abAB", "abAB"),
    ]

    for input_str, expected in test_cases:
        result = sol.makeGood(input_str)
        assert result == expected, f"Expected {expected}, but got {result}"
    print("All tests passed!")