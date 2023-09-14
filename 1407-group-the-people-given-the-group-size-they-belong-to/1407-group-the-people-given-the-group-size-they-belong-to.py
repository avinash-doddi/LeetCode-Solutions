class Solution:
    def groupThePeople(self, arr: List[int]) -> List[List[int]]:
        from collections import defaultdict as maps
        d = maps(lambda : [0,[]])
        n = len(arr)
        fin = []
        for i in range(n):
            d[arr[i]][0] += 1; d[arr[i]][1].append(i);
            if d[arr[i]][0] == arr[i]:
                d[arr[i]][0] = 0; 
                fin.append(d[arr[i]][1]);
                d[arr[i]][1] = [];
        return fin