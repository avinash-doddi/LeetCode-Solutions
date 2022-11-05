class Solution:
    def traverse(self, strr, s, n, r, i, j):
        self.i = i; self.j = j;
        if (i > n or i <= 0 or self.k >= n): return
        strr[i][j] = s[self.k]; self.k += 1;
        self.traverse(strr, s, n, r, i-1, j+1);
        
    
    def convert(self, s: str, r: int) -> str:
        if (r == 1): return s
        n = len(s);
        strr = [[""]*900 for i in range(r)];
        self.k = 0; self.i = 0; self.j = 0;
        while(self.k < n):
            if (self.i == r-1):
                #self .i -= 1; self.j += 1;
                self.traverse(strr, s, n, r, self.i, self.j);
            else:
                strr[self.i][self.j] = s[self.k];
                self.i += 1; self.k += 1;
        finalstr = ''
        for lst in strr:
            finalstr += ("".join(lst));
        return finalstr
            
            
            
                
                
                
        