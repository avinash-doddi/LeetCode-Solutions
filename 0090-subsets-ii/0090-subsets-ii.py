class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]; d = {}
        for num in nums:
            for i in range(len(subsets)):
                currSubset = subsets[i]
                subsets.append(currSubset + [num])
        for sub in subsets: 
            sub.sort();
            d[tuple(sub)] = 1;
        subsets.clear();
        for sub in d.keys(): subsets.append(list(sub));
        return subsets