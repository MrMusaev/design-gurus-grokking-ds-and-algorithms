# https://leetcode.com/problems/valid-parentheses/description/ 
class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {
            ')': '(', 
            ']': '[', 
            '}': '{'
        }
        stack = []

        for p in s:
            # If the parenthesis is opening one
            if p not in parenthesis:
                stack.append(p)
                continue

            # If stack is empty, we have closing p without opening. If closing and opening one doesn't match, then we have a wrong pair
            if not stack or parenthesis[p] != stack.pop():
                return False    
        
        # If anything left in the stack, we don't have enough closing paranthesis 
        return len(stack) == 0
    
# Unit tests with expected and actual results
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = {
        "()" : True,
        "()[]{}" : True,
        "(]" : False,
        "([)]" : False,
        "{[]}" : True,
        "" : True,
        "(((" : False,
        ")))" : False,
        "([])" : True
    }
    
    for s, expected in test_cases.items():
        result = solution.isValid(s)
        print(f"Input: {s}, Expected: {expected}, Result: {result}, Passed: {expected == result}")
