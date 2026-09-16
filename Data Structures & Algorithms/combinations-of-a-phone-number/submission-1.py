class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        q = list(digits)

        hashmap = {"2": ["a","b","c"],
                   "3": ["d","e","f"],
                   "4": ["g","h","i"],
                   "5": ["j","k","l"],
                   "6": ["m","n","o"],
                   "7": ["p","q","r","s"],
                   "8": ["t","u","v"],
                   "9": ["w","x","y","z"],
                   }

        res = []
        def dfs(i, curr):
            if i == len(digits):
                res.append(curr)
                return

            for letter in hashmap[q[i]]:
                dfs(i + 1, curr + letter)

        dfs(0, "")
        return res