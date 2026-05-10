class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            res.append(prefix)
            prefix = prefix * nums[i]

        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        return res