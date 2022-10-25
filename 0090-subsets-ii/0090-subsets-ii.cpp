class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& arr) {
        vector<vector<int>> fin;
        map<vector<int>, long int> mp;
        long long int i, j, n = arr.size();
        for (i = 0; i < pow(2, n); i++)
        {
            vector<int> b;
            for (j = 0; j < n; j++)
            {
                if (i & (1<<j))
                {
                    b.push_back(arr[j]);
                }
            }
            sort(b.begin(), b.end());
            mp[b] ++;
        }
        for (auto it: mp)
        {
            fin.push_back(it.first);
        }
        return fin;
    }
};