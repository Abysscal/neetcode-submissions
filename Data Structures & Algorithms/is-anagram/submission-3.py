class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shash, thash = {},{}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            shash[s[i]] = shash.get(s[i],0)+1
            thash[t[i]] = thash.get(t[i],0)+1
        
        if shash == thash:
            return True
        else:
            return False