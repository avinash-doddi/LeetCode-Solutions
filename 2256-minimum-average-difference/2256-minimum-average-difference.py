class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefixSum=[nums[0]]
        for i in nums[1:]:
            prefixSum.append(prefixSum[-1]+i)
        suffixSum=[0 for i in range(len(nums)+1)]
        for i in range(len(nums)-1,-1,-1):
            suffixSum[i]=suffixSum[i+1]+nums[i]
        mindiff=float("inf")
        minind=-1
        for i in range(len(nums)):
            # print(prefixSum,i)
            diff= abs((prefixSum[i]//(i+1)) - (suffixSum[i+1]//max(len(nums)-(i+1),1) ) ) 
            if diff<mindiff:
                minind=i
                mindiff=diff 
            if diff==0:
                return i
        return minind
        
        