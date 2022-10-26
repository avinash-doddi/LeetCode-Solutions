class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size(); int start = 0, end = n - 1;
        vector<int> arr(n);
        while(start <= end)
        {
            if (nums[start]*nums[start] <= nums[end]*nums[end])
            {
                arr[end - start] = nums[end]*nums[end];
                end -= 1;
            }
            else
            {
                arr[end - start] = nums[start]*nums[start];
                start ++;
            }
        }
        return arr;
    }
};