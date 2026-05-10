class Solution:
    def climbStairs(self, n: int) -> int:
      
        dp = [0] * (n + 2)
        dp[1], dp[2] = 1,2

        def dfs(val):
            if val > n:
                return
            
            dp[val] = dp[val-1] + dp[val-2]
            dfs(val + 1)
            dfs(val + 2)

        dfs(3)

        return dp[n]