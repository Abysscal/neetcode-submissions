class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <2:
            return nums[0]
        memo = [-1] * len(nums)
        memo[-1] = nums[-1]
        memo[-2] = nums[-2]

        def dfs(pos):
            if pos + 2 > len(nums)-1:
                return nums[pos]

            if memo[pos] == -1:
                inLarge = -1
                for i in range(pos + 2, len(nums)):
                    val = dfs(i)
                    if val > inLarge:
                        inLarge = val
                memo[pos] = inLarge + nums[pos]

            return memo[pos]





        for i in range(len(nums)-1, -1, -1):
            dfs(i)


        return max(memo)