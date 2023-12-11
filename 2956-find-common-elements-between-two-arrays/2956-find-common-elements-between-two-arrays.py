class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import defaultdict as maps
        d1 = maps(int); d2 = maps(int)
        for i in nums1: d1[i] += 1;
        for i in nums2: d2[i] += 1;
        return [sum([1 if d2[i] else 0 for i in nums1]),sum([1 if d1[i] else 0 for i in nums2])]
        