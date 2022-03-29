class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # DP array S, where S[j] is the largest contiguous array
        # sum with
        S = [0] * len(nums)
        S[0] = nums[0]
        for i in range(1, len(nums)):
            # either include current element or include
            # sum of subsequence upto that element
            S[i] = max(nums[i], S[i-1] + nums[i])
        return max(S)