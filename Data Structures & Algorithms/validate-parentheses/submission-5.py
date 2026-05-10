class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        slist = list(s)
        if len(slist) % 2 != 0:
            return False

        while len(slist) >0:
            temp = slist.pop(0)
            if temp in "({[":
                stack.append(temp)
            else:
                if len(stack)==0:
                    return False
                l = stack[-1]
                if l == '(' and temp == ')':
                    stack.pop()
                elif l == '{' and temp == '}':
                    stack.pop()
                elif l == '[' and temp == ']':
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        else:
            return True
                