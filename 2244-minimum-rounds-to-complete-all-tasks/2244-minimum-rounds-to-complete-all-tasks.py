from collections import Counter as c
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = c(tasks);
        flag = 0; tc = 0
        for x,y in freq.items():
            if y < 2: 
                flag = 1; break
            elif y % 3 == 0:
                tc += y//3
            elif y % 3 == 1:
                tc += 2; y -= 4;
                tc += y//3;
            elif y % 3 == 2:
                tc += 1; y -= 2;
                tc += y//3;
            elif tc % 2 == 0:
                tc += y//2;
        if flag: return -1
        return tc
                
                