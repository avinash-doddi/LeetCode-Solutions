from collections import deque

class StockSpanner:

    def __init__(self):
        self.list = deque(); 

    def next(self, price: int) -> int:
        count = 1;
        if (self.list):
            i = len(self.list) - 1;
            
            while i >= 0 and self.list[i][0] <= price:
                count += self.list[i][1];
                i -= self.list[i][1];
            
        self.list.append((price, count));
        return count;
                


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)