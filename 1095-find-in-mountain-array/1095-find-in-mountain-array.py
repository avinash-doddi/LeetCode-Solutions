# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, m: 'MountainArray') -> int:
        #find peak::
        n = m.length(); left = 0; right = n-1;
        mid = 0; peak = -1; peak_index = -1; calls = 0
        
        while left <= right:
            # mid = (left + right)//2;
            mid = left + (right - left)//2
            if mid < 0 or mid > n-1: break
            curr = m.get(mid);
            before, after = m.get(mid-1), m.get(mid+1)
            calls += 3;
            if before < curr > after:
                peak = curr; peak_index = mid; break;
            # else::
            if curr < after:
                left = mid; 
            elif curr < before:
                right = mid;
                
        if peak == target: return peak_index
        
        # check leftside of array::
        left = 0; right = peak_index;
        while left <= right:
            mid = left + (right - left)//2
            if mid < 0 or mid > peak_index: break
            curr = m.get(mid); calls += 1;
            if curr == target: 
                return mid;
            #else::
            if curr < target:
                left = mid+1;
            else:
                right = mid-1;
            
        # check rightside of array::
        print(peak_index)
        left = peak_index; right = n-1;
        while left <= right:
            mid = left + (right - left)//2;
            if mid < peak_index or mid > n-1: break
            curr = m.get(mid);
            if curr == target:
                return mid;
            #else::
            if curr > target:
                left = mid+1;
            else:
                right = mid-1;
        
        #if element not present::
        return -1
            
            
        
        
        