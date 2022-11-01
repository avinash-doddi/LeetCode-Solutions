#User function Template for python3
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self,w,I,n):
        items = []
        for i in I:
            items.append([i.weight, i.value]);
        items.sort(key = lambda x: x[1]/x[0], reverse = True);
        total = 0
        for item in items:
            if (w >= item[0]):
                total += item[1]; w -= item[0];
            elif (w > 0):
                total += ((item[1]/item[0])*w); w = 0;
            else: break
        return total
                
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.2f" %ob.fractionalknapsack(W,Items,n))

# } Driver Code Ends