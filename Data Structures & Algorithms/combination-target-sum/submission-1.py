class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(pointer, curList, total):
            if total == target:
                res.append(curList.copy())
                return None
            if pointer >= len(nums) or total > target:
                return None

            curList.append(nums[pointer])
            dfs(pointer, curList, total + nums[pointer])
            curList.pop()
            dfs(pointer + 1, curList, total)

        dfs(0,[], 0)
        return res