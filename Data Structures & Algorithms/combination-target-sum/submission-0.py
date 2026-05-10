class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(i,path,total):
            if total == target:
                finalPath.append(path.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            path.append(nums[i])
            dfs(i, path, total + nums[i])
            path.pop()
            dfs(i+1, path, total)
            
        

        finalPath = []
        dfs(0,[],0)

        return finalPath