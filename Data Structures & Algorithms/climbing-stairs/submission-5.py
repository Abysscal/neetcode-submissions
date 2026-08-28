class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        table = [0] * (n+1)
        table[1] = 1
        table[2] = 2
        def dp(n):
            if table[n] != 0:
                return table[n]

            table[n] = dp(n-1) + dp(n-2)

            return table[n]

        return dp(n)