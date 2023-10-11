class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True); processorTime.sort();
        n = len(processorTime); maxx = 0; pt = 0;
        for i in range(0,4*n,4):
            maxx = max(maxx, processorTime[pt] + max(tasks[i],tasks[i+1],tasks[i+2],tasks[i+3]))
            pt += 1;
        return maxx;
        
        