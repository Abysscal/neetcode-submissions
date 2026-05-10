class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            wordmap = [0] * 26
            for c in word:
                wordmap[ord(c) - ord('a')] += 1
            hashmap[tuple(wordmap)].append(word)
        
        return list(hashmap.values())
