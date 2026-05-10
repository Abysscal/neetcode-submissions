class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setList = set()

        for i in nums:
            if i in setList:
                return True
            else:
                setList.add(i)

        return False