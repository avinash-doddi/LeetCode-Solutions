from sortedcontainers import SortedDict as maps
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = maps()
        for i in nums:
            if i in d:
                d[i] += 1;
            else: d[i] = 1;
        index = 0;
        for x,y in d.items():
            if (y == 1):
                nums[index] = x; index += 1;
            else:
                temp = 2;
                while(temp > 0):
                    nums[index] = x; index += 1; temp -= 1;
        return index;