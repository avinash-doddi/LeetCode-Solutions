from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ispresent = defaultdict(bool);
        index = defaultdict(int);
        index1 = defaultdict(int);
        n = len(numbers);
        for i in range(n):
            ispresent[numbers[i]] = True;
            if (index[numbers[i]] != 0):
                index1[numbers[i]] = (i+1);
            if (index[numbers[i]] == 0):
                index[numbers[i]] = (i+1);
        indices = []; ref = 0; ind1 = 0; ind2 = 0;
        for i in range(n):
            ref = (target - numbers[i]);
            if (ispresent[ref]):
                ind1 = index[numbers[i]]
                ind2 = index[ref];
                if (ind1 == ind2):
                    ind2 = index1[ref];
                if (ind2 != 0):
                    indices.append(ind1);
                    indices.append(ind2); break
        return indices