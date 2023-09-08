class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = 34
        rows = [[1]]; tmp = []; cnt = 1;
        while (n > 1):
            if cnt == 1:
                cnt += 1; rows.append([1,1])
            else:
                tmp = [rows[-1][0]];
                for i in range(cnt-1):
                    tmp.append(rows[-1][i] + rows[-1][i+1]);
                tmp.append(rows[-1][-1]); cnt += 1;
                rows.append(tmp); 
            n -= 1;
        return rows[rowIndex]