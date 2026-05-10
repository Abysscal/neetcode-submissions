class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        shash, thash = [0] * 26, [0] * 26

        for i in range(len(s)):
            shash[ord(s[i])-ord('a')] += 1
            thash[ord(t[i])-ord('a')] += 1
        
        if shash == thash:
            return True
        else:
            return False
