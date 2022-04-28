class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int i=0;
        while(i<n-2){
            int j=i+1; int k = n -1;
            int target = nums[i] * -1;
            while(j<k){
                int low = nums[j];
                int high = nums[k];
                if(nums[j] + high == target){
                    ans.push_back({nums[i], nums[j], high});
                    while(j<k && nums[j] == low) j++;
                    while(k>j && nums[k] == high) k--;
                }
                else if(nums[j] + nums[k] < target){
                    while(j<k && nums[j] == low) j++;
                }else{
                    while(k>j && nums[k] == high) k--;
                }
            }
            int curr = nums[i];
            while(i<n-2 && nums[i] == curr) i++;
        }
        return ans;
    }
};
