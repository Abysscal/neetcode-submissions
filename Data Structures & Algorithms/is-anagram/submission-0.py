class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapperA, mapperB = {}, {}

        for i in s:
            if i not in mapperA:
                mapperA[i] = 0
            mapperA[i] += 1

        for i in t:
            if i not in mapperB:
                mapperB[i] = 0
            mapperB[i] += 1

        if mapperA == mapperB:
            return True
        else: 
            return False