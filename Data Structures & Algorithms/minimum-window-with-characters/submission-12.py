class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have, need = 0, len(set(t))
        shash, thash = {},{}
        size =float('inf')
        l =0
        res = [0,0]
        for i in t:
            thash[i] = thash.get(i,0) + 1

        for r in range(len(s)):
            c = s[r]
            shash[c] = shash.get(c,0) + 1
            if c in thash and shash[c] == thash[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < size:
                    size = r-l+1
                    res = l,r
                
                shash[s[l]] -= 1
                if s[l] in thash and shash[s[l]] < thash[s[l]]:
                    have -= 1
                l+= 1
        return s[res[0]:res[1]+1] if size != float('inf') else "" 

        