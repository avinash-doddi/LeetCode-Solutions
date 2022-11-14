#User function Template for python3
class Solution:
    def numberOfSubsequences (self,s,w):
        # code here 
        count = 0; n = len(s); m = len(w);
        s = [i for i in s]
        for i in range(n):
            k = 0;
            for j in range(i, n):
                if (s[j] == w[k]):
                    s[j] = '0';
                    k += 1;
                if (k == m):
                    count += 1; break;
        return count
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())
        W=str(input())

        ob = Solution()
        print(ob.numberOfSubsequences(S,W))

# } Driver Code Ends