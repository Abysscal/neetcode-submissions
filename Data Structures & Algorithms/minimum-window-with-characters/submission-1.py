class Solution:
    def minWindow(self, s: str, t: str) -> str:
            if len(t) == 0:
                return ""

            tDict, wordDict = {}, {}
            res, resLen = [-1,-1] , float('inf')
            l = 0
            for i in t:
                tDict[i] = 1 + tDict.get(i, 0)

            have, need = 0, len(tDict)
            for r in range(len(s)):
                c = s[r]
                wordDict[c] = 1 + wordDict.get(c, 0)

                if c in tDict and wordDict[c] == tDict[c]:
                    have += 1

                while have == need:
                    if (r-l+1) < resLen:
                        resLen = r-l+1
                        res[0], res[1] = l, r

                    wordDict[s[l]] -=1
                    if s[l] in tDict and wordDict[s[l]] < tDict[s[l]]:
                        have -= 1
                    l += 1

            
            return s[res[0]:res[1]+1]



