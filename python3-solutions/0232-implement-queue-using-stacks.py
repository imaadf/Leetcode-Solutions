class MyQueue:

    def __init__(self):
        self.size = 0
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            raise IndexError

        self.move()
        self.size -= 1

        return self.output_stack.pop()

    def peek(self) -> int:
        if self.size == 0:
            raise IndexError

        self.move()

        return self.output_stack[-1]

    def empty(self) -> bool:
        return self.size == 0

    def move(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
