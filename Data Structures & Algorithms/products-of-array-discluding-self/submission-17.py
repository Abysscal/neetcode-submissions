class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post =1,1
        prefix, postfix = [[0] for i in range(len(nums))],[[0] for i in range(len(nums))]

        for i in range(len(nums)):
            prefix[i] = pre
            pre *= nums[i]
        print(prefix)
        for i in range(len(nums)-1, -1,-1):
            postfix[i] = post
            post *= nums[i]
        print(postfix)

        res = []

        for i in range(len(nums)):
            res.append(prefix[i]*postfix[i])
        return res
