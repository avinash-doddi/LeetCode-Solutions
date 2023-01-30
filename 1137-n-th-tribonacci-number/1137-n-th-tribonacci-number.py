class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n==0: return 0
        elif n==1: return 1
        elif n==2: return 1
        elif n==3: return 2
        else:    
            a,b,c,s = 0,1,1,2
            
            for i in range(n-2):
                s = (a+b+c)
                t=a
                a=b
                b=c
                c=s

                if i==n-1:
                    return c

        return c