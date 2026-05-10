class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        pre, post = 1,1

        for i in range(len(nums)):
                prefix[i] = pre
                pre *= nums[i]
        
        for i in range(len(nums)-1,-1,-1):
                postfix[i] = post
                post *= nums[i]

        res = []
        for i in range(len(nums)):
            res.append(prefix[i]*postfix[i])

        return res
        