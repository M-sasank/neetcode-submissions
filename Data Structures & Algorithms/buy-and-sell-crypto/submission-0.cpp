class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // min_total = INT_MAX;
        int max_total = prices[0];

        if(size(prices)<2){
            return 0;
            }
        
        int i = 1;
        int maxProfit = INT_MIN;
        while(i<size(prices)){
            if (max_total > prices[i]){
                max_total = prices[i];
            }

            int profit = prices[i] - max_total;
            if (maxProfit < profit){
                maxProfit = profit;
            }
            i++;
        }

        return maxProfit>0 ? maxProfit:0;
        
    }
};
