class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            wordList = [0] * 26
            for c in word:
                wordList[ord(c)-ord('a')] += 1
            if tuple(wordList) not in res:
                res[tuple(wordList)] = []
            res[tuple(wordList)].append(word)

        return list(res.values())