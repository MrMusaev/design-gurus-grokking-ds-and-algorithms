class Solution: 
    def decimalToBinary(self, num):
        stack = []
        
        if num == 0:
            return '0'
        
        while num > 0:
            stack.append(num % 2)
            num //= 2

        result = ''
        while stack:
            result += str(stack.pop())

        return result

# Tests with assertions
if __name__ == "__main__":
    solution = Solution()
    test_cases = {
        0: '0',
        1: '1',
        2: '10',
        3: '11',
        4: '100',
        5: '101',
        6: '110',
        7: '111',
        8: '1000',
        9: '1001',
        10: '1010'
    }

    for num, expected in test_cases.items():
        result = solution.decimalToBinary(num)
        print(f"Input: {num}, Expected: {expected}, Result: {result}, Passed: {expected == result}")