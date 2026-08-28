class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,0
        if n <=2:
            return n

        for i in range(n):
            temp = one
            one = one + two
            two = temp

        return one