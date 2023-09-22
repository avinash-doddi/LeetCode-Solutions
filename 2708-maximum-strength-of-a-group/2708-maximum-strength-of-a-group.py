class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        pos = []; neg = []; negcnt = 0; poscnt = 0; n = len(nums)
        for i in nums:
            if i < 0: 
                neg.append(i); negcnt += 1;
            else: 
                pos.append(i); poscnt += 1;
        if poscnt == 1 and negcnt == 0: return pos[0]
        if negcnt == 1 and poscnt == 0: return neg[0]
        pos.sort(reverse = True); neg.sort()
        if 0 in pos: 
            pos = [i for i in pos if i]
        if negcnt & 1: neg = neg[0:negcnt - 1]
        total = 1;
        if pos or neg:
            for i in pos: total *= i
            for i in neg: total *= i
            return total
        else: return 0
        
        
            
        
        
        