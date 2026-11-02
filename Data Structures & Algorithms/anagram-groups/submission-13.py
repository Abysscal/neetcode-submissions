class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listofwords = defaultdict(list)

        for word in strs:
            hashset = [0] * 26
            for c in word:
                hashset[ord(c) - ord("a")] += 1
            listofwords[tuple(hashset)].append(word)

        res = []
        for key,v in listofwords.items():
            res.append(v)
        return res
