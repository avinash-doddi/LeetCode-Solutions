class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        init = 1; fin = []
        for i in target:
            for j in range(init, n+1):
                fin.append("Push"); 
                if i == init:
                    break;
                else: 
                    init += 1; fin.append("Pop");
            init += 1;
        return fin