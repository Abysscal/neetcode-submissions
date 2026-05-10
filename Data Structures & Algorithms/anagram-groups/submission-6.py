class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resdict = {}

        for str in strs:
            strhash = [0] * 26
            for c in str:
                strhash[ord(c) - ord("a")] += 1
            res = tuple(strhash)
            if res not in resdict:
                resdict[res] = []
            resdict[res].append(str)

        return list(resdict.values())