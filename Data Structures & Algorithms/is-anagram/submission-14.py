class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = [0] * 26 
        hash2 = [0] * 26
        for c in s:
            hash[ord(c) - ord('a')] += 1

        for c in t:
            hash2[ord(c) - ord('a')] += 1

        if hash2 == hash:
            return True

        return False