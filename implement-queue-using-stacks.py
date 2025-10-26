class MyQueue:

    def __init__(self):
        self.inputs: list[int] = []
        self.outputs: list[int] = []

    def push(self, x: int) -> None:
        self.inputs.append(x)

    def pop(self) -> int:
        self._transfer()
        return self.outputs.pop()

    def peek(self) -> int:
        self._transfer()
        return self.outputs[-1]

    def empty(self) -> bool:
        return len(self.inputs) == 0 and len(self.outputs) == 0

    def _transfer(self) -> None:
        if len(self.outputs) == 0:
            while len(self.inputs) > 0:
                self.outputs.append(self.inputs.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()