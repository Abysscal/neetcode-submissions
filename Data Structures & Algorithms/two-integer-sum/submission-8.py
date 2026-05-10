class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        sSorted = sorted(nums)

        l,r = 0,len(nums)-1

        while sSorted[l] + sSorted[r] != target:
            if sSorted[l] + sSorted[r] > target:
                r -=1
            elif sSorted[l] + sSorted[r] < target:
                l+=1

        num1 = sSorted[l]
        num2 = sSorted[r]
        num1pos = None
        for i in range(len(nums)):
            if nums[i] == num1 and num1pos == None:
                num1pos = i
            elif nums[i] == num2:
                num2pos = i
   

        return sorted([num1pos, num2pos])