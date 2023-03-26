from bisect import bisect_left as bb
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort(); n = len(nums); ans = []
        prefix = []; summ = 0; req = 0
        for i in nums:
            summ += i; prefix.append(summ);
        for i in queries:
            index = bb(nums, i, 0, n); req = 0;
            if index == n or index == 0:
                req = abs(prefix[n-1] - (n*i))
            elif i == nums[index]:
                temp = prefix[n-1] - prefix[index];
                diff = (n-1-index)*i;
                req += abs(temp - diff); #right
                if index > 0:
                    temp = prefix[index];
                    diff = (index+1) * i;
                    req += abs(temp - diff); #left
            else:
                if index != 0: index -= 1;
                temp = prefix[n-1] - prefix[index];
                diff = (n-1-index)*i;
                req += abs(temp - diff); #right
                if index >= 0:
                    temp = prefix[index];
                    diff = (index+1)*i;
                    req += abs(temp - diff); #left
            ans.append(req);
        return ans

                
                
                