from random import choice
class RandomizedSet:

    def __init__(self):
        self.sett = set()
        

    def insert(self, val: int) -> bool:
        if (val in self.sett): return False;
        self.sett.add(val); return True

    def remove(self, val: int) -> bool:
        try:
            self.sett.remove(val);
        except KeyError:
            return False
        return True;
        

    def getRandom(self) -> int:
        return choice(list(self.sett))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()