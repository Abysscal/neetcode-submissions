class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        pre = 1
        post = 1
        for i in range(len(nums)):
            prefix[i] = pre
            pre = nums[i] * pre

        for i in range(len(nums)-1, -1, -1):
            postfix[i] = post
            post = nums[i] * post

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])

        return res
