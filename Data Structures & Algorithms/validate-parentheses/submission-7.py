class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeAndOpen = {')' : '(', '}' : '{', ']' : '['}

        for c in s:
            if c in closeAndOpen:
                if stack and stack[-1] == closeAndOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
