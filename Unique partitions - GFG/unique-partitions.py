#User function Template for python3

class Solution:
	def UniquePartitions(self, n):
		# Code here
		arr = [i for i in range(n,0,-1)]
		ref = []; fin = []; target = n
		def recur(arr, i, n, ref, target, fin):
		    if (target == 0):
		        fin.append(ref[:])
		        return
		    if (i == n or target < 0): return
	        ref.append(arr[i])
	        recur(arr, i, n, ref, target-arr[i], fin)
	        ref.pop()
	        recur(arr, i+1, n, ref, target, fin);
		       
		    
        recur(arr, 0, n, ref, target, fin)
        return fin;


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n= int(input())
		ob = Solution()
		ans = ob.UniquePartitions(n)
		for a in ans:
			for b in a:
				print(b, end = " ")
		print()

# } Driver Code Ends