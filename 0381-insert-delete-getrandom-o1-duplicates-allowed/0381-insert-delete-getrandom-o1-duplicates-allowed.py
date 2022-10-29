from random import choice
from sortedcontainers import SortedList as listt
class RandomizedCollection:

    def __init__(self):
        self.sett = listt()
        

    def insert(self, val: int) -> bool:
        if (val in self.sett):
            self.sett.add(val); return False
        else:
            self.sett.add(val); return True

    def remove(self, val: int) -> bool:
        try:
            self.sett.remove(val);
        except ValueError:
            return False
        return True;
        

    def getRandom(self) -> int:
        return choice(self.sett)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()