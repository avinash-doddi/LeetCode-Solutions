class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []; n = len(height); maxx = 0;
        for i in range(n):
            maxx = max(maxx,height[i]);
            prefix.append(maxx);
        suffix = []; maxx = 0;
        for i in range(n-1,-1,-1):
            maxx = max(maxx,height[i]);
            suffix.append(maxx);
        print(prefix,suffix); suffix.reverse()
        finalsum = 0
        for i in range(n):
            finalsum += min(prefix[i],suffix[i])-height[i];
        return finalsum