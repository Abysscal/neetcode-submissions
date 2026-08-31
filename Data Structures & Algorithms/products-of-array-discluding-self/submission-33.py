class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1,1
        prearr, postarr = [], deque()

        # pre
        for i in nums:
            prearr.append(pre)
            pre = pre*i
        
        #post
        for i in range(len(nums)-1, -1, -1):
            postarr.appendleft(post)
            post = post* nums[i]

        for i in range(len(prearr)-1):
            prearr[i] = prearr[i] * postarr[i]

        return prearr