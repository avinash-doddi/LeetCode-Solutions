class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr); summ = 0; temp = 0; cnt = 0;
        for i in range(n):
            temp = 0; cnt = 0;
            for j in range(i, n):
                temp += arr[j]; cnt += 1;
                if cnt & 1:
                    summ += temp;
        return summ;