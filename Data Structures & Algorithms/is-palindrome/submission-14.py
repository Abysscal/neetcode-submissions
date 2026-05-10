class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaOnly = ''
        for c in s:
            if c.isalnum():
                alphaOnly += c.lower()
        reverse = alphaOnly[::-1]
        print(reverse)
        if alphaOnly == reverse:
            return True
        else:
            return False
        