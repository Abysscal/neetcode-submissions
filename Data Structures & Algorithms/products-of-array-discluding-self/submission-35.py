class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prelist, postlist = [1] * len(nums), [1] * len(nums)
        prenum, postnum  = 1,1

        for i in range(len(nums)):
            prelist[i] = prenum
            prenum *= nums[i]
        
        for k in range(len(nums)-1, -1, -1):
            postlist[k] = postnum
            postnum *= nums[k]
        
        res = []
        for i in range(len(nums)):
            res.append(prelist[i]*postlist[i])
        
        return res