from sortedcontainers import SortedSet as s
from collections import defaultdict as maps
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        mp = maps(s); n = len(s1);
        for i in range(n):
            mp[s1[i]].update(s2[i]);
            mp[s2[i]].update(s1[i]);
            mp[s1[i]].update(mp[s2[i]]);
            mp[s2[i]].update(mp[s1[i]]);
        check = [0]*26;
        print(check)
        for i in s1: check[ord(i) - 97] = 1;
        for i in s2: check[ord(i) - 97] = 1;
        print(check)
        for i in range(26):
            if check[i]:
                temp = s();
                temp.update(mp[chr(i+97)]);
                for j in mp[chr(i+97)]:
                    temp.update(mp[j]);
                mp[chr(i+97)] = temp; check[i] = 0;
                for j in mp[chr(i+97)]:
                    mp[j] = temp; check[ord(j) - 97] = 0;
        print(mp);
        returnstr = ''
        for i in baseStr:
            if i in mp:
                returnstr += mp[i][0];
            else:
                returnstr += i;
        return returnstr