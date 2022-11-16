class Solution {
public:
    int count = 0;
    void recur(vector<int> &arr, int target, int i, int n)
    {
        if (n <= i)
        {
            if (target == 0) count += 1;
            return;
        }
        recur(arr, target+arr[i], i+1, n);
        recur(arr, target-arr[i], i+1, n);
    }
    
    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        recur(nums, target, 0, n);
        return count;
    }
};