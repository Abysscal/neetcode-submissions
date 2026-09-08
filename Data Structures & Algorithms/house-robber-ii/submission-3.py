class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        def robber(un):
            dp = [-1] * len(un)
            dp[0] = un[0]
            dp[1] = max(un[0], un[1])
            for i in range(2, len(un)):
                dp[i] = max(un[i] + dp[i-2], dp[i-1])

            return dp[-1]
        
        return max(robber(nums[1:]), robber(nums[:-1]))
            