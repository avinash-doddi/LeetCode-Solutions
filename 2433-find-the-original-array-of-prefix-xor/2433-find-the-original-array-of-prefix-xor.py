class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        returnarr = []; n = len(pref)
        for i in range(n):
            if (i == 0):
                returnarr.append(pref[i]);
            else:
                returnarr.append(pref[i-1]^pref[i]);
        return returnarr