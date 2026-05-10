class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for word in strs:
            # a - z
            count = [0] * 26

            for c in word:
                count[ord(c)-ord("a")] += 1
            hashMap[tuple(count)].append(word)

        return list(hashMap.values())