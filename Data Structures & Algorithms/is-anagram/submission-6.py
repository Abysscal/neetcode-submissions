class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = [0] * 28

        tMap = [0] * 28

        for i in s:
            sMap[ord(i) - ord("a")] += 1

        for i in t:
            tMap[ord(i) - ord("a")] += 1

        if sMap == tMap:
            return True
        return False
