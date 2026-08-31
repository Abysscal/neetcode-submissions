class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for word in strs:
            wmap = [0] * 26
            for c in word:
                wmap[ord(c) - ord('a')] += 1
            hashmap[tuple(wmap)].append(word)
        
        return list(hashmap.values())
