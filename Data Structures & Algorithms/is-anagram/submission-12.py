class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap, tMap = {},{}

        for i in s:
            sMap[i] = sMap.get(i,0) + 1
        for i in t:
            tMap[i] = tMap.get(i, 0) + 1

        if sMap == tMap:
            return True
        return False
