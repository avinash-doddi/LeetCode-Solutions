class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> mp, mp1; vector<int> arr;
        long long int i, val = 0;
        for (i = 0; i < nums.size(); i++)
        {
                mp[nums[i]] += 1;
                mp1[nums[i]] = i;
        }
        for (i = 0; i < nums.size(); i++)
        {
                val = target - nums[i];
                if (val == nums[i])
                {
                    if (mp[nums[i]] >= 2)
                    {
                        arr.push_back(i);
                        arr.push_back(mp1[val]);
                        return arr;
                    }
                }
                else
                {
                    if (mp[val] > 0)
                    {
                        arr.push_back(i);
                        arr.push_back(mp1[val]);
                        return arr;
                    }
                }
            }
        return arr;
    }
};