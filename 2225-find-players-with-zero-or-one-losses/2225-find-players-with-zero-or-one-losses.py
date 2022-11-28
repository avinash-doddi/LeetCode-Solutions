from collections import defaultdict as maps
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = maps(int); loss = maps(int);
        for w, l in matches:
            win[w] += 1; loss[l] += 1;
        winners = [x for x in win.keys() if loss[x] == 0]
        losers = [x for x in loss.keys() if loss[x] == 1]
        winners.sort(); losers.sort()
        return [winners, losers]