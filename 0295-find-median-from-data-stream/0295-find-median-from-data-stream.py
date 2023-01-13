from sortedcontainers import SortedList as SL
class MedianFinder:

    def __init__(self):
        self.slist = SL([]); self.size = 0;

    def addNum(self, num: int) -> None:
        self.slist.add(num); self.size += 1;

    def findMedian(self) -> float:
        if self.size & 1:
            return self.slist[self.size//2];
        else:
            return (self.slist[self.size//2 - 1] + self.slist[self.size//2])/2;
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()