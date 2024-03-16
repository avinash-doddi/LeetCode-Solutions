class Solution:
    def minimizeStringValue(self, s: str) -> str:
        from collections import defaultdict as maps, deque as dq
        d = maps(int)
        
        for i in s: d[i] += 1
                   
        finArr = ""
        toadd = []
        
        for i in s:
            if i == "?":
                maxx = 10**8; curr = ""
                for i in range(97, 123):
                    if d[chr(i)] < maxx:
                        maxx = d[chr(i)]; curr = chr(i);
                
                toadd.append(curr); 
                d[curr] += 1;
                       
        toadd = dq(sorted(toadd));
        #print(toadd)
        for i in s:
            if i == "?":
                finArr += toadd.popleft()
            else:
                finArr += i
        return finArr
            
                
            
            
        