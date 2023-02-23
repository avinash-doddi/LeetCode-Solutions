class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums); one = 0;
        try:
            d = {0:[]}; zro = 0; start = -1;
            maxx, end = -1,0; temp = 0;
            for i in range(n):
                end = i;
                if start == -1:
                    start = i;
                if nums[i] == 0:
                    if zro == k:
                        temp = d[0][0]; d[0].append(i);
                        del d[0][0]; start = temp+1;
                    else:
                        d[0].append(i); zro += 1;
                maxx = max(maxx, end - start+1);
            return max(maxx, end - start+1)
        except Exception:
            maxx = 0;
            for i in range(n):
                if nums[i] == 1:
                    one += 1;
                else:
                    one = 0;
                maxx = max(maxx, one);
            return maxx
                    
        