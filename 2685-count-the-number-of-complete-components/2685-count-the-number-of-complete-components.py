class Graph:
    
    def __init__(self,n):
        self.cnt = n
        self.arr = [i for i in range(n)]
        
    def find(self, x):
        if self.arr[x] == x: return x
        return self.find(self.arr[x]);
    
    def combi(self, x, y):
        self.arr[self.find(x)] = self.find(y)
        
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        node = Graph(n);
        
        for a,b in edges:
            node.combi(a,b);
        
        xmp, ref = {}, {}
        for i in range(n):
            xmp[node.find(i)] = 0;
            if node.find(i) not in ref:
                ref[node.find(i)] = 0;
            ref[node.find(i)] += 1;
        
        for a,b in edges:
            x,y = node.find(a), node.find(b);
            if x == y: xmp[x] += 1;
        
        tt = 0;
        for a,b in xmp.items():
            if ref[a]*(ref[a] - 1)//2 == b:
                tt += 1;
        return tt