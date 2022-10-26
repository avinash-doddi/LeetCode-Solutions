class LUPrefix:

    def __init__(self, n: int):
        self.videos = set();
        self.long = 0
        #return None

    def upload(self, video: int) -> None:
        self.videos.add(video);
        while self.long + 1 in self.videos:
            self.long += 1;
                

    def longest(self) -> int:
        return self.long


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()