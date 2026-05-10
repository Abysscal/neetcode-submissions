class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        res = [0] * len(nums)

        for i in range(len(nums)):
            if i != 0:
                pre = pre * nums[i-1]
            res[i] = pre


        # 1, 1, 2, 8
        for i in range(len(nums)-1, -1, -1):
            if i != len(nums)-1:
                post = post * nums[i+1]
            res[i] = post * res[i]

        return res
