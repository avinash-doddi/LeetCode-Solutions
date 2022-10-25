class Solution {
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        long long int i, j, n = nums.size();
        vector<vector<int>> fin;
        map<vector<int>, int> mp;
        for (i = 0; i < pow(2,n); i++)
        {
            vector<int> b;
            for (j = 0; j < n; j++)
            {
                if (i & (1 << j))
                {
                    b.push_back(nums[j]);
                }
            }
            if (is_sorted(b.begin(), b.end()) and b.size() > 1)
            {
                mp[b]++;
            }
        }
        for (auto it: mp) fin.push_back(it.first);
        return fin;
    }
};