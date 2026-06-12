class Solution:
    def isPalindrome(self, s: str) -> bool:
        charOnly = ""
        s = s.lower()

        for c in s:
            if c.isalnum():
                charOnly += c

        print(charOnly)
        return charOnly == charOnly[::-1]