class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int length = nums.size();
        int* maxSubArrayTill = new int[length]; // maximum subarray until index [i] of nums, containing index [i]
        int max = maxSubArrayTill[0] = nums[0];
        // Complete because all contiguous array will end in an index in range
        for (int i = 1; i < length; ++i) {
            maxSubArrayTill[i] = nums[i] + ((maxSubArrayTill[i - 1] > 0)?maxSubArrayTill[i - 1]:0);
            //                                                  /\
            //                                 We can choose not to take maximum contiguous array up until i - 1
            //                                    so we will choose between 0 and maximum contiguus subarray
            max = (max > maxSubArrayTill[i])?max:maxSubArrayTill[i]; 
            // Inline max computations
        }
        return max;
    }
};
/**
    If we have a[j:i] being the maximum contiguous subarray from a[0:i], with 0 <= j <= i, 
        then if a_{i + 1} is positive, a[j..i+1] will be the maximum contiguous subarray
    So, how about checking for maximum contiguous subarray ending at index i?
 */