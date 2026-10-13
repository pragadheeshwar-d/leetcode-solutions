class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        int n = nums.size();
        for (auto& num : nums) {
            num *= num;
        }
        sort(nums.begin(), nums.end());

        long long sum = 0;

        for (int i = 0; i < n / 2; i++)
            sum -= nums[i];

        for (int i = n / 2; i < n; i++)
            sum += nums[i];

        return sum;
    }
};