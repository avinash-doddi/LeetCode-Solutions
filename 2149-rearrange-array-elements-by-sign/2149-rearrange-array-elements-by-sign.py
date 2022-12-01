class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []; neg = []; p , n = 0, 0;
        for i in nums: 
            if (i > 0): 
                pos.append(i); p += 1;
            else:
                neg.append(i); n += 1;
        newarr = []; c = 0; f = 0; i = 0; j = 0;
        while(p > 0 and n > 0):
            if (c == 0):
                newarr.append(pos[i]);
                p -= 1; c += 1; f = 1; i += 1;
            else:
                if (f):
                    newarr.append(neg[j]);
                    n -= 1; j += 1;  c += 1; f = 0;
                else:
                    newarr.append(pos[i]);
                    p -= 1; i += 1; c += 1; f = 1;
        while(p > 0):
            newarr.append(pos[i]);
            i += 1; p -= 1;
        while (n > 0):
            newarr.append(neg[j]);
            j += 1; n -= 1;
        return newarr
                
        
            
        