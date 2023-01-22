from collections import defaultdict as maps
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        matrix = maps(list);
        n = len(score); m = len(score[0]);
        for i in range(n): matrix[i] = score[i];
        index = [i for i in range(n)]; scr = {i:score[i][k] for i in range(n)};
        index.sort(key = lambda x: scr[x], reverse = True);
        score = [matrix[i] for i in index];
        return score