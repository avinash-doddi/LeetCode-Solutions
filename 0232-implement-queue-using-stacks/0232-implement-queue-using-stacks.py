class MyQueue:

    def __init__(self):
        self.list = []
        self.top = 0

    def push(self, x: int) -> None:
        self.list.append(x); self.top += 1;

    def pop(self) -> int:
        self.top -= 1;
        return self.list.pop(0);
    

    def peek(self) -> int:
        return self.list[0];

    def empty(self) -> bool:
        return not bool(self.top)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()