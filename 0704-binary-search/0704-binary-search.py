class Solution:
    def search(self, a: List[int], x: int) -> int:
        n = len(a); low, high = 0, n-1;
        while low <= high and x >= a[low] and x <= a[high]:
            if low == high:
                if a[low] == x:
                    return low
                return -1
            
            pos = low + int(((high-low)/(a[high]-a[low])) * (x - a[low]));
            
            if x == a[pos]: return pos
            if x < a[pos]:
                high = pos - 1;
            else: 
                low = pos + 1
        return -1
            
                