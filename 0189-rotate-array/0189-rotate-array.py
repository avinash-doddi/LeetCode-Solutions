class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums); k = k % n;
        self.val = nums[:]; j = 0;
        for i in range(n-k, n):
            nums[i], nums[j] = nums[j], nums[i]; j += 1;
        i = k;
        for j in range(0,n-k):
            nums[i] = self.val[j]; i += 1;