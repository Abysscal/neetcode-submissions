class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlpha(s):
            return (ord(s) >= ord('a') and ord(s) <= ord('z')) or (ord(s) >= ord('0') and ord(s) <= ord('9'))

        l,r = 0, len(s)-1

        while l < r :
            while l < r and not isAlpha(s[l].lower()):
                l += 1
            while r > l and not isAlpha(s[r].lower()):
                r-= 1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True