class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1,1
        prefix, postfix = [0] * len(nums), [0] * len(nums)
        res = [0] * len(nums)

        for i in range(len(nums)):
            prefix[i] = pre
            pre *= nums[i]

        for i in range(len(nums)-1, -1,-1):
            postfix[i] = post
            post *= nums[i]

        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]

        return res