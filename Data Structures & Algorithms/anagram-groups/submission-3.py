class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for s in word:
                count[ord(s) - ord('a')] += 1
            hashTable[tuple(count)].append(word)

        return list(hashTable.values())