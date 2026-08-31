class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap, tmap = {},{}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            schar = s[i]
            tchar = t[i]
            smap[schar] = 1 + smap.get(schar,0)
            tmap[tchar] = 1 + tmap.get(tchar,0)
        
        return smap == tmap