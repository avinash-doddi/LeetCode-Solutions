#User function Template for python3
from collections import defaultdict as maps
class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        d = maps(int); pos = 0;
        for i in arr:
            if i > 0: 
                d[i] += 1;
                pos = 1;
        if not pos:
            return 1
        else:
            for i in range(1, max(arr)+2):
                if d[i] == 0:
                    return i;


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            print(ob.missingNumber(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends