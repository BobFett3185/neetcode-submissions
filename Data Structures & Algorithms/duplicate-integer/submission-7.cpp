class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> myset;
        for (int i=0; i< nums.size(); i++) {
            if (myset.count(nums[i])) {
                return true;
            }
            myset.insert(nums[i]);
        }
    return false;
        
    }
};

/*
NOT OPTIMAL
for(int i = 0; i < nums.size(); i++)
            for(int j=0 ; j< nums.size(); j++)
                if (nums[i] == nums[j] && i != j )
                    return true; 

        return false; 
*/