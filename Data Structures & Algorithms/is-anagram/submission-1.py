class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashA = {}
        hashB = {}

        for i in range(len(s)):
            if s[i] not in hashA:
                hashA[s[i]] = 0
            if t[i] not in hashB:
                hashB[t[i]] = 0
            hashA[s[i]] += 1
            hashB[t[i]] += 1

        if hashA == hashB:
            return True
        else:
            return False