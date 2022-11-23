#User function Template for python3
class Solution:
    def maxSumLCM (self, n):
        # code here 
        sum = 0; sq = int(n**0.5);
        for i in range(1, sq+1):
            if (n % i == 0): 
                if ((n//i)*(n//i) == n): sum += n//i;
                else: sum += (i + n//i);
        return sum
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.maxSumLCM(n))
# } Driver Code Ends