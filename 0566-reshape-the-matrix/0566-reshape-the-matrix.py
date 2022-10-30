import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        new = np.array(mat);
        try:
            new = new.reshape(r,c);
        except ValueError:
            new = mat;
        return list(new)