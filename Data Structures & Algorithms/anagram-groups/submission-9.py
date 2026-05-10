class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashStr = defaultdict(list)
        
        for word in strs:
            wordMap = [0] * 26
            for c in word:
                wordMap[ord(c) - ord('a')] += 1
            hashStr[tuple(wordMap)].append(word)

        return list(hashStr.values())
    
