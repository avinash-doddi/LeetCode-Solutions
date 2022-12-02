from collections import defaultdict as mp
class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 0; s = ''; j = 0; n = 0; ref = ''; val = 0
        char = chars[:]
        for i in char:
            if (s == ''):
                s = i; count += 1;
            elif (i == s): count += 1;
            else:
                if (count == 1):
                    chars[val] = s; s = i; val += 1; count = 1;
                elif (count <= 9):
                    chars[val] = s; val += 1;
                    chars[val] = str(count); val += 1;
                    s = i; count = 1;
                else:
                    ref = str(count); n = len(ref); count = 1
                    chars[val] = s; s = i; val += 1; j = 0;
                    while(n > 0):
                        chars[val] = ref[j];
                        val += 1; j += 1; n -= 1;
        if (count == 1):
            chars[val] = s; s = i; val += 1; count = 1;
        elif (count <= 9):
            chars[val] = s; val += 1;
            chars[val] = str(count); val += 1;
            s = i; count = 1;
        else:
            ref = str(count); n = len(ref);
            chars[val] = s; s = i; val += 1; j = 0;
            while(n > 0):
                chars[val] = ref[j];
                val += 1; j += 1; n -= 1;
                
                
        return val
        