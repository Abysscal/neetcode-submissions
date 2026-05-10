class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finallist = []
        for i in range(len(nums)):
            tempList = nums.copy()
            del tempList[i]
            number = 1
            for k in tempList:
                number = number * k
            finallist.append(number)

        return finallist

