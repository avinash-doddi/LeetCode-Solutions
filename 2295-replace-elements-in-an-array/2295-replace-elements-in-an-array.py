class Solution:
    def arrayChange(self, arr: List[int], oper: List[List[int]]) -> List[int]:
        d = {}; n = len(arr);
        for i in range(n): d[arr[i]] = i;
        for x, y in oper:
            index = d[x];
            arr[index] = y; d[y] = index;
        return arr