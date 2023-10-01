class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict as maps
        #links = maps(lambda : maps(int))
        cnt = maps(int);
        for a,b in roads:
            cnt[a] += 1;
            cnt[b] += 1;
        cities = [i for i in cnt]
        cities.sort(reverse = True, key = lambda x: cnt[x])
        print("cities", cities)
        imp = [0 for i in range(n)]
        tmp = n; n = len(cities)
        for i in range(n):
            imp[cities[i]] = tmp; tmp -= 1;
        total = 0
        for a,b in roads:
            total += imp[a] + imp[b]
        return total
        
        
        