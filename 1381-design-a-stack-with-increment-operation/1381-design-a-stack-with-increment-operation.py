class CustomStack:

    def __init__(self, maxSize: int):
        self.size = -1;
        self.max = maxSize
        self.stk = [];

    def push(self, x: int) -> None:
        if (self.size+1 < self.max):
            self.stk.append(x); self.size += 1;
        print("push called", self.stk)


    def pop(self) -> int:
        print("pop called", self.stk)
        if (self.size == -1): return -1
        val = self.stk.pop(); self.size -= 1;
        return val

    def increment(self, k: int, val: int) -> None:
        if (k <= self.size):
            for i in range(k):
                print(self.stk[i], i);
                self.stk[i] += val;
        else:
            for i in range(self.size+1):
                print(self.stk[i], i);
                self.stk[i] += val;
        print(self.stk)


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)