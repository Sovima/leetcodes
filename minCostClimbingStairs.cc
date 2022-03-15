class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int l = cost.size();
        if ( l == 1 ) {
            return cost[0];
        }
        int price1 = cost[0];
        int price2 = cost[1];
        for ( int i = 2; i < l ; ++i ) {
            int temp = cost[i] + min(price1, price2);
            price1 = price2;
            price2 = temp;
        }
        return min(price1, price2);
        
    }
};
