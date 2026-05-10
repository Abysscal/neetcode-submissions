class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1, 1
        prearray, postarray = [],[]

        for i in nums:
            prearray.append(pre)
            pre = pre*i

        for i in range(len(nums)-1, -1, -1):
            postarray.insert(0,post)
            post = post*nums[i]

        for i in range(len(prearray)-1):
            prearray[i] = prearray[i] * postarray[i]

        return prearray
