class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones = []; n = len(boxes); c = 0; returnarr = []; total = 0
        for i in range(n):
            if (boxes[i] == '1'): 
                ones.append(i); c += 1;
        for i in range(n):
            total = 0;
            for j in range(c):
                total += abs(i - ones[j]);
            returnarr.append(total);
        return returnarr
            