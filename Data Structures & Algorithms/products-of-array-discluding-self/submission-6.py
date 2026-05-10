class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        res = [0] * len(nums)

        for i in range(len(nums)):
            res[i] = pre
            pre = nums[i] * pre

        for i in range(len(nums)-1, -1, -1):
            res[i] = post * res[i]
            post = nums[i] * post

        return res

