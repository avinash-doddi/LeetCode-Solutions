class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict as maps
        cnt = maps(int);
        d = maps(lambda: maps(int))
        for a,b in roads:
            if d[a][b] == 0:
                d[a][b] = 1; cnt[a] += 1;
            if d[b][a] == 0:
                d[b][a] = 1; cnt[b] += 1;
        maxx = 0;
        for i in range(n):
            for j in range(n):
                if i != j:
                    if d[i][j]:
                        maxx = max(maxx, (cnt[i]+cnt[j]-1));
                    else:
                        maxx = max(maxx, (cnt[i]+cnt[j]));
        return maxx
        