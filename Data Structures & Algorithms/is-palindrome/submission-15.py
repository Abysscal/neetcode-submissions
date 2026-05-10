class Solution:
    def isPalindrome(self, s: str) -> bool:
        trim = []

        for c in s:
            if c.isalnum():
                trim.append(c.lower())
            
        reverse = trim[::-1]
        return trim == reverse