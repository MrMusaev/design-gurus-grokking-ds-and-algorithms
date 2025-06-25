class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue2.append(x)

        while self.queue1:
            self.queue2.append(self.queue1.pop(0))
        
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        if self.empty():
            return None
        
        return self.queue1.pop(0)      

    def top(self) -> int:
        if self.empty():
            return None
        
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1


# Tests with assertions
if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    assert stack.pop() == 2
    assert not stack.empty()
    assert stack.pop() == 1
    assert stack.empty()
    
    # Additional test cases
    stack.push(3)
    assert stack.top() == 3
    assert not stack.empty()
    stack.push(4)
    assert stack.top() == 4
    assert not stack.empty()
    
    print("All tests passed!")