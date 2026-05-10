class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return []
        res= []
        nums = sorted(nums)

        for i in range(len(nums)):
            l,r = i+1, len(nums)-1

            if i != 0 and nums[i] == nums[i-1]:
                continue
            while l<r:
                three = nums[i] + nums[l] + nums[r]
                print(nums[i] , nums[l], nums[r])
                if three < 0:
                    l+=1
                elif three >0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l +=1


        return res

            