class Solution:
    # Can be broken down into subproblems.
    # You can either start a new subarray for a maximum sum at index i
    # or you could add the element at index i to the previous subproblem.
    
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(dp[i-1] + nums[i], nums[i]))
        return max(dp)