class Solution:
    def search(self, a: List[int], k: int) -> int:
        s = 0; e = len(a) - 1; mid = (s + e)//2;
        if (a[mid] == k): return mid;
        while(s < e):
            mid = (s+e)//2;
            if (a[mid] == k): return mid;
            if (a[mid] < k): s = mid+1;
            if (a[mid] > k): e = mid-1;
        if (a[s] == k): return s;
        if (a[e] == k): return e;
        else: return -1
                