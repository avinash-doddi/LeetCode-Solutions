from collections import defaultdict as maps
class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        lst = []; n = len(s);
        d = maps(int); i = 0;
        while (n > i):
            if (lst):
                ins = 0;
                new = maps(int);
                for j in s[i]:
                    new[j] += 1;
                for sublst in lst:
                    if (sublst[0] == new):
                        sublst.append(s[i]); ins = 1;
                        break;
                if (ins == 0):
                    lst.append([new, s[i]]);
                del new;
                    
            else:
                del d; d = maps(int);
                for k in s[i]:
                    d[k] += 1;
                lst.append([d, s[i]]);
            i += 1;
        for sublst in lst:
            del sublst[0]
        return lst
                
        
