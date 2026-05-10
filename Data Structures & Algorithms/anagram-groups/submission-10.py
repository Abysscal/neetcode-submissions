class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            wordHash = [0]*26
            for c in word:
                wordHash[ord(c) - ord('a')] += 1
            hashmap[tuple(wordHash)].append(word)

        return list(hashmap.values())
    
