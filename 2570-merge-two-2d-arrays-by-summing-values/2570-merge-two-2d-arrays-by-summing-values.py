from collections import defaultdict as maps
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = maps(int);
        for a,b in nums1: d[a] = b;
        for a,b in nums2: d[a] += b;
        newarr = []
        for i in sorted(d.keys()):
            newarr.append([i, d[i]]);
        return newarr
        