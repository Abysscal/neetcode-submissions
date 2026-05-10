class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        postfix = []

        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(prefix[i-1] * nums[i-1])

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                postfix.append(1)
            elif len(postfix) == 1:
                postfix.insert(0,postfix[0] * nums[i+1])
            else:
                postfix.insert(0,postfix[0] * nums[i+1])

        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])
        return res