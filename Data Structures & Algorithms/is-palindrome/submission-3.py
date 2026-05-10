class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        filtering = []
        for c in s:
            if (ord(c) >= ord('0') and ord(c) <= ord('9')) or ord(c) >= ord('a') and ord(c) <= ord('z'):
                filtering.append(c)
        
        letters = "".join(filtering)

        if len(letters) ==0:
            return True

        l,r = 0, len(letters)-1
        mid = len(letters) //2
        while l != mid+1:
            if letters[l] != letters[r]:
                return False
            l += 1
            r -= 1
        return True
