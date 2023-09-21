from sortedcontainers import SortedList
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = SortedList([x for x in nums1] + [x for x in nums2]);
        l = len(s);
        if (l & 1):
            return s[l//2];
        return (s[l//2 - 1] + s[l//2])/2;