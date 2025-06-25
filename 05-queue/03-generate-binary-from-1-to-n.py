class Solution:
    def generateBinaryNumbers(self, n):
        res = []
        q = ["1"]

        for i in range(n):
            q.append(q[i] + "0")
            q.append(q[i] + "1")
            res.append(q[i])
        
        return res

# Tests with assertions
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (1, ["1"]),
        (2, ["1", "10"]),
        (3, ["1", "10", "11"]),
        (4, ["1", "10", "11", "100"]),
        (5, ["1", "10", "11", "100", "101"]),
        (6, ["1", "10", "11", "100", "101", "110"]),
        (7, ["1", "10", "11", "100", "101", "110", "111"]),
    ]

    for n, expected in test_cases:
        result = sol.generateBinaryNumbers(n)
        assert result == expected, f"Expected {expected}, but got {result}"
    
    print("All tests passed!")