class Solution {
public:
    vector<vector<int>> subsets(vector<int>& arr) {
        vector<vector<int>> fin;
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
            fin.push_back(b);
        }
        return fin;
    }
};