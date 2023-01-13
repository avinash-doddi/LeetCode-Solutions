class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        sort(costs.begin(), costs.end());
        long long int buy = 0;
        for (auto it: costs)
        {
            if (it > coins)
                break;
            buy += 1; coins -= it;
        }
        return buy;
    }
};