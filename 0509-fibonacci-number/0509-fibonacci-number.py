class Solution:

    def __init__(self):
        self.fibnocci = [0,1,1,2]
        for i in range(4,46):
            self.fibnocci.append(self.fibnocci[i-1]+self.fibnocci[i-2]);
            
    def fib(self, n: int) -> int:
        return self.fibnocci[n]
        