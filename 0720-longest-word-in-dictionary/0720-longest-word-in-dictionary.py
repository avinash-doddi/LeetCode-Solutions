from collections import defaultdict as maps
class Solution:
    def longestWord(self, words: List[str]) -> str:
        freq = maps(int); lenn = maps(list)
        letter = {ch:len(ch) for ch in words}
        words.sort(); flag = 0;
        for word in words:
            if len(word) == 1: freq[word] += 1;
            else:
                flag = 0; prev = ''; s = ''; i = 0;
                for ch in word:
                    s += ch; i += 1;
                    if (freq[s]):
                        prev = s;
                    else:
                        if (i == 1): # if 1st letter is not present, we don't even consider that word...
                            flag = 1; break;
                        elif (letter[word] > (letter[prev]+1)):
                            flag = 1; break;
                        else:
                            freq[word] += 1;
            if (not flag):
                lenn[len(word)].append(word);
        if (lenn):
            maxx = max(lenn);
            lenn[maxx].sort(); return lenn[maxx][0]
        return ""
            
                    
                