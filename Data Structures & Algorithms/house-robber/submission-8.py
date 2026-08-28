class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        first = nums[0]
        second = max(nums[0], nums[1])
        dp = [-1] * (len(nums))
        dp[0] = first
        dp[1] = second

        def dps(unit):
            if dp[unit] != -1:
                return dp[unit]
            dp[unit] = max(dps(unit-2) + nums[unit], dps(unit-1))
            return dp[unit]

        return dps(len(nums)-1)