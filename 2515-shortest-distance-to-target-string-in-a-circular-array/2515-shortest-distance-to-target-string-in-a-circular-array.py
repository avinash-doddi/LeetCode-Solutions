class Solution:
    def closetTarget(self, words: List[str], target: str, st: int) -> int:
        try:
            x = words.index(target)
            if words[st] == target: return 0;
            #move fwd
            n = len(words)
            count = 0; x = ''; i = st + 1
            while x != target:
                if i == n:
                    i = 0;
                if x == target: break
                x = words[i]; i += 1; count += 1;
            #move backward
            count1 = 0; x = ''; i = st - 1
            while x != target:
                if i == -1:
                    i = n-1;
                if x == target: break
                x = words[i]; i -= 1; count1 += 1;
            return min(count, count1)

        except Exception:
            return -1